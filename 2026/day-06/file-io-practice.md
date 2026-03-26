# Read and Write text files in Linux

* `touch notes.txt`

   Create a textfile with name notes.txt

* `echo "Hi, I am arvind" > notes.txt`

   Write to notes.txt

* `echo "I am a devops enthusiast" >> notes.txt`

  `echo "Today is day06 of learning linux" >> notes.txt`
  
   Append to notes.txt

* `cat notes.txt`

   Read notes.txt

* `cat notes.txt | head -n 1`

   Read first line of notes.txt

* `cat notes.txt | tail -n 2`

   Read last two lines of notes.txt

* `echo "Learn using tee command" | tee -a notes.txt`
<img width="1281" height="688" alt="image" src="https://github.com/user-attachments/assets/d4eef12b-ae4f-470e-876a-8f1ec01be512" />

Summary:
- Read: cat, less, head, tail, tee
- Write: echo, nano, touch, vi, vim.
