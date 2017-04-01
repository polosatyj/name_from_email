In some cases, you need to know the real user name, while you only have its email (or for example nickname). This script in Python processes the list of emails and tries to identify the real user name by filing the result in a new file (the part of the e-mail before @). For example, you have a list of emails in a text file as:
Oxana@domain.com
Roman@domen2.com
Ivan@domen3.com
You run the script and on the output you have a new file, like:
Oxana; oxana@domen.com
Roman; roman@domen2.com
Ivan; ivan@domen3.com
After that, you can export the result to your database (or program) and then refer to the user using his real name.
The script defines names by the concomitant transcription database of the most popular names (325 most popular names - the database is presented in a separate file, available for editing).
To run the script, Python 2.7 must be installed on your system, which is available for all operating systems on the official Python site - python.org


To load the initial list of emails - copy it to the folder with the script as emailes.txt (or correct the value of this variable in the script itself under the name of your file).
The result will be written to the file named_emails.csv (or correct the value of this variable in the script itself under the name of your file).
To run the script in Windows, double-click on the executable script file.

-------------------------------------------------------
� ��������� ������� ���������� ������ �������� ��� ������������, � �� ����� ��� � ��� ������� � ������� ������ ��� ����� (���� �������� ���). ���� ������ �� Python ������������ ������ ������� � �������� �� ���� (����� ������ ����� @) ���������� �������� ��� ������������, ��������� ��������� � ����� ����. � ������� � ��� ���� ������ ������� � ��������� ����� � ����:
oxana@domen.com
roman@domen2.com
ivan@domen3.com
�� ���������� ������ � �� ������ ������ ����� ����, ����:
������;oxana@domen.com
�����;roman@domen2.com
����;ivan@domen3.com
����� ���� ������� �������������� ��������� � ���� ���� (��� ���������) � ���������� ������ � ������������ ��������� ��� �������� ���.
������ ���������� ����� �� ������������� ���� ������������ �������� ���������� ���� (325 ����� ���������� ���� - ���� ������������� � ��������� �����, ��������� ��� ��������������).
��� ������� ������� � ���� ������� ������ ���� ���������� Python 2.7, ������� �������� ��� ���� �� �� ����������� ����� Python - python.org


��� �������� ��������� ������ ������� - ���������� ��� � ����� �� �������� ��� ������ emailes.txt (���� ��������� �������� ���� ���������� � ����� ������� ��� ��� ������ �����).
��������� ��������� � ���� named_emails.csv (���� ��������� �������� ���� ���������� � ����� ������� ��� ��� ������ �����).
��� ������� ������� � �� Windows ������ �������� �� ����������� ����� �������.