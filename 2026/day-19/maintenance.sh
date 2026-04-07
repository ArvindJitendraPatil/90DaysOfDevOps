#!/bin/bash

log_rotation(){
	
	~/scripts/2026/day-19/log_rotate.sh /var/log/myapp >> sudo /var/log/maintenance.log
}

backup(){
	 ~/scripts/2026/day-19/backup.sh ~/downloads ~/demo >> sudo /var/log/maintenance.log
}

main(){  #-e means - escape sequences like \n
	echo -e "\n$(date) : Starting Maintenance... " >> sudo /var/log/maintenance.log
	log_rotation
	backup
	echo "Maintenance completed for today" >> sudo /var/log/maintenance.log
}

main
echo "Successfully written logs to /var/log/maintenance.log"
