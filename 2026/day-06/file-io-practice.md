Linux Fundamentals: Read & Write Text Files
1. Reading Files:
 cat filename.txt
 less filename.txt
 head filename.txt
 tail filename.txt
 tail -f filename (live logs)
2. Writing / Creating Files:
 echo 'text' > file.txt (overwrite)
 echo 'text' >> file.txt (append)
 touch file.txt (create empty file)
 nano file.txt (edit file)
 printf 'Line1\nLine2' > file.txt
3. Useful Combinations:
 cp a.txt b.txt
 cat a.txt b.txt > merged.txt
 wc file.txt (line/word/char count)
Summary:
Read: cat, less, head, tail, tail -f
Write: echo, printf, nano, touch
