#!/bin/bash
#sleep 30s
rm -Rf /home/vagrant/.local/share/fieldworks/Projects/hel*
/home/vagrant/Integration-Testing-Framework/sikuli/sikuli_no_remove_runall.sh
#for D in `find /home/vagrant/Integration-Testing-Framework/sikuli/*.sikuli -type d`
#do
#	ps cax | grep mono > /dev/null
#	if [ $? -eq 0 ]; then
#	  echo Running $D ...
#	  echo Running $D ... >> /vagrant/error_log
#          sikuli $D
#          rm /home/vagrant/*.png > /dev/null
#	else
#	  echo "FLEX is not running."
#	  echo "FLEX is not running." >> /vagrant/error_log
#	  exit #break
#	fi
#done
