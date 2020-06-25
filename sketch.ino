#define red 3
#define green 5
#define blue 6
#define button 4

/*--------------------------------------------------------------------*/

int time=10;
int i = 0;
void setup(){
	pinMode(red,OUTPUT);
	pinMode(green,OUTPUT);
	pinMode(blue,OUTPUT);
	pinMode(button,INPUT_PULLUP);
	Serial.begin(9600);
	Serial.setTimeout(50);
}
void loop(){
	if (digitalRead(button)==0){
	//	delay(100);
		do
		{
			for (int i = 0; i < 255; i++) {
				analogWrite(green,i);
				delay(time);
			}
			for (int i = 0; i < 255; i++) {
				analogWrite(red,i);
				delay(time);
			}
			for (int i = 255; i > -1; i--) {
				analogWrite(green,i);
				delay(time);
			}
			for (int i = 0; i < 255; i++) {
				analogWrite(blue,i);
				delay(time);
			}
			for (int i = 255; i > -1; i--) {
				analogWrite(red,i);
				delay(time);
			}
			for (int i = 0; i < 255; i++) {
				analogWrite(green,i);
				delay(time);
			}
			for (int i = 255; i > -1; i--) {
				analogWrite(green,i);
				delay(time);
			}
			for (int i = 255; i > -1; i--) {
				analogWrite(blue,i);
				delay(time);
			}
		}while (digitalRead(button)!=0);
		if (digitalRead(button==0)){
			delay(1000);
			analogWrite(red,0);analogWrite(green,0);analogWrite(blue,0);
		}
	}
	/*-----------------------------------------------------------------------------------------------*/
	if (Serial.available() > 1){
		char key=Serial.read();
		int val = Serial.parseInt();
		switch(key){
			case 'r' : analogWrite(red,val); break;
			case 'g' : analogWrite(green,val); break;
			case 'b' : analogWrite(blue,val); break;
			case 'a' : analogWrite(red,val);analogWrite(green,val);analogWrite(blue,val); break;
			case 's' : time=val; break;
			default :
				while (Serial.available() <= 0){
					for (int i = 0; i < 255; i++) {
						analogWrite(green,i);
						delay(time);
					}
					for (int i = 0; i < 255; i++) {
						analogWrite(red,i);
						delay(time);
					}
					for (int i = 255; i > -1; i--) {
						analogWrite(green,i);
						delay(time);
					}
					for (int i = 0; i < 255; i++) {
						analogWrite(blue,i);
						delay(time);
					}
					for (int i = 255; i > -1; i--) {
						analogWrite(red,i);
						delay(time);
					}
					for (int i = 0; i < 255; i++) {
						analogWrite(green,i);
						delay(time);
					}
					for (int i = 255; i > -1; i--) {
						analogWrite(green,i);
						delay(time);
					}
					for (int i = 255; i > -1; i--) {
						analogWrite(blue,i);
						delay(time);
					}
				}
			break;
		}
	}
}
