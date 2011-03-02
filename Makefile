
all:

sql-setup:
	@mysql -u xscore -pxscorepass < etc/setup.sql
