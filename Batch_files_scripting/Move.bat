@echo off
md MyDocuments
md MyImages
md MyMp3
md MyVideos
md AndroidSoftwares

move *.txt "MyDocuments"
move *.pdf "MyDocuments"
move *.docx "MyDocuments"
move *.jpg "MyImages"
move *.jpeg "MyImages"
move *.png "MyImages"
move *.gif "MyImages"
move *.mp3 "MyMp3"
move *.m4a "MyMp3"
move *.aac "MyMp3"
move *.mp4 "MyVideos"
move *.apk "AndroidSoftwares"