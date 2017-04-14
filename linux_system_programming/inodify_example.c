#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/inotify.h>

/* A buffer big enough to read 100 events */
#define BUFFSIZE (100 * (sizeof(struct inotify_event) + NAME_MAX +1))


void main()
{
    FILE *fileconfig; /* File Descriptor for config file */
    FILE *fileout; /* File Descriptor for output file */
    char watchname[PATH_MAX];

    struct stat sb;

    int notifyfd, watchfd;

    char eventbuff[BUFFSIZE];
    int n;

    char *p;

    struct inotify_event *event;

    char warchednamed[100][NAME_MAX+1];

    notifyfd = inotify_init();

    /* Open the config file */

    if((fileconfig = fopen("monitor.conf", "r")) ==  NULL) {
	printf("Unable to open the config file; giving up!\n");
        exit(1);
    }

    /* Read all watched file names from config file */
    while (fgets(watchname, PATH_MAX, fileconfig) !=NULL){
	/*Get rid of the newlline */
        watchname[strlen(watchname)-1] = '\0';

	if(state(watchname, &sb) < 0){
	    printf("Cannot stat %s, ignored\n", watchname);
	    continue;
	}
	
	if(S_ISREG(sb.st_mode)) {
	    /*Regular file, so add to watch list */
	    if ((watchfd = inotify_add_watch(notifyfd, watchname, IN_MODIFY | IN_DELETE_SELF)) < 0) {
		printf("error adding watch for %s\n", watchname);
		} else {
		    printf("added %s to watch list on descriptor %d\n", watchname, watchfd);
		    /* Record the file we're watching on this watch descriptor */
		    strcpy(watchednames[watchfd], watchname);
		}
	} else { /*Probably a directory */
	    printf("%s is not a regular file, ignored\n", watchname);
	}
    }


    /* All our watches are in plcae, so just read and report events */
    fileout = fopen("monitor.out", "a");

    while(1) {
	n = read(notifyfd, eventbuff, BUFFSIZE);
        /* Loop over all events and report them. This is a little tricky becasue the 
	event records are not of fixed length */

	for (p = eventbuff; p < eventbuff + n;) {
	    event = (struct inotify_event *)p;
	    p += sizeof(struct inotify_event) + event->len;
	    /*Display the event*/
	    if (event->mask & IN_MODIFY) fprintf(fileout, "%s was modified\n", watchednames[event->watchfd]);
	    if (event->mask & IN_DELETE_SELF) fprintf(fout, "%s was deleted\n", watchednames[event->watchfd]);	
	    fflush(fileout);
	}
    }
}

