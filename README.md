🧠 How it works

Simulates a login system

Tracks failed attempts per IP

Detects brute-force behavior

Blocks attackers automatically

Logs incidents for investigation


🧪 Test it (attack simulation)

Run the server:

python bruteforce_detector.py


Simulate an attack (PowerShell):

for ($i=0; $i -lt 10; $i++) {


  Invoke-RestMethod -Uri http://127.0.0.1:5000/login `

  
  -Method POST `

  
  -Body '{"username":"admin","password":"wrong"}' `

  
  -ContentType "application/json"

  
}




📂 Output artifacts (for your portfolio)
security.log → shows attack evidence

Code → shows defensive logic

Attack simulation → shows red-team awareness
