/* please also see: http://www.lafn.org/~dave/linux/Serial-Programming-HOWTO-B.txt */
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <termios.h>
#include <stdio.h>
#include <string.h>

#define DEVICE_INTERFACE "/dev/ttyUSB0"
void sendcmd(const int fd, const char *cmd);
void receivedata(const int fd);

int main(int argc, char *argv[])
{
	int fd, res;
	struct termios oldtio,newtio;
	char buf[255]={0,};

	fd = open(DEVICE_INTERFACE, O_RDWR | O_NOCTTY );
	if (fd <0) {perror(DEVICE_INTERFACE); return 1; }

	tcgetattr(fd,&oldtio); /* save current port settings */

	bzero(&newtio, sizeof(newtio));

	newtio.c_cflag = B9600 | CRTSCTS | CS8 | CLOCAL | CREAD;
	newtio.c_iflag = IGNPAR;
	newtio.c_oflag = 0;
	newtio.c_lflag = 0;

	newtio.c_cc[VTIME]    = 5;
	newtio.c_cc[VMIN]     = 0;

	tcflush(fd, TCIFLUSH);
	tcsetattr(fd,TCSANOW,&newtio);

	char CR[]={0x0D,0};
	char LF[]={0x0A,0};
	char XON[]={0x11,0};
	char XOFF[]={0x13,0};
	char REMOTE_ENABLE[]={0x14,0};
	char REMOTE_DISABLE[]={0x12,0};
	
	char *IDN="*IDN?";
	char *EVTS="EVTS?";
	char *TIME="TIME?";

	sendcmd(fd, REMOTE_ENABLE);
	sendcmd(fd, XON);
	sendcmd(fd, IDN);
//	sendcmd(fd, CR);
	sendcmd(fd, LF);
	receivedata(fd);

	int n;
	char c, cmd[128];
	int lines=0;
	while (1){
		lines++;
		n=0;
		if(lines == 1) printf("Note: press enter will sent LF, press Ctrl-D to exit.\n");
		printf("Please Enter Command: ");
		while (c = getc(stdin)) {
			if (c == EOF)goto out;
			cmd[n]=c;
			n++;
			if(c == 0x0A)break;
//			printf("debug: %x\n", c);
		}
		if(n==0)break;
		else cmd[n]=0;

		sendcmd(fd, cmd);
		//sendcmd(fd, LF);
		receivedata(fd);
	}

out:
	sendcmd(fd, REMOTE_DISABLE);
	tcsetattr(fd,TCSANOW,&oldtio);
}

void sendcmd(const int fd, const char *cmd)
{
	int res = 0;
	res = fwrite(fd,cmd,strlen(cmd));
	//printf("send command: %s , %d bytes\n",cmd,res);
}
void receivedata(const int fd)
{
	char buf[256]={0,};
	int res;
	while(1)
	{
		res = fread(fd,buf,255);
		if(res > 0 ){
			buf[res]=0;
			printf("%s", buf);
			//printf("buf:%s res:%d\n", buf, res);
		}else{
			//printf("No data return! %d \n", res);
			break;
		}
	}
}
