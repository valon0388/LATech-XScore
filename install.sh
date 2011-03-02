#!/bin/bash
set -e

echo '=================== Installing XScore ==============================='
echo "Installing XScore..."

echo '=================== External Dependencies ==========================='
DEPENDS="python2.6
         python-paramiko 
         python-mysqldb
         mysql-server
         python-twisted"

echo "Installing external dependencies..."
aptitude install $DEPENDS
echo "External dependencies installed."
echo

echo '=================== MySQL set up ===================================='
echo "XScore will need to create a MySQL user account."
echo "Please provide a MySQL user name with the appropriate"
echo "  permissions to create this user."
read -p 'MySQL User: ' usr
read -s -p 'MySQL Password: ' passwd
echo

echo "Creating MySQL user..."
mysql -u $usr -p$passwd -e "DROP USER xscore" 2> /dev/null || true
mysql -u $usr -p$passwd <<'EOF'
  GRANT ALL ON scores.* TO 'xscore'@'localhost' IDENTIFIED BY 'xscorepass';
  GRANT ALL ON scores.* TO 'xscore'@'%';
EOF
usr=; passwd=;
echo "MySQL user created."

echo "Initializing MySQL database..."
make sql-setup
echo "MySQL database initialized."
echo

echo 'XScore installed.'
