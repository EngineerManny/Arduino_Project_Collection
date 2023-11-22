#include <avr/io.h>
#include <util/delay.h>

int main(void) {

	DDRB = 0; // Sets all bits in the data direction register for PORTB to 0 making all of the pins in PORTB inputs. 
	DDRA |= (1 << PA0); // Sets PORTA pin 0 (Digital Pin 22) to 1 making it an output.

	while(1) {

		PORTA |= (1 << PA0); // Sets PORTA pin 0 (Digital Pin 22) to 1 making it high.
		_delay_ms(1000); // waits 1 second
		PORTA &= ~(1 << PA0); // sets PORTA pin 0 (Digital Pin 22) to 0 making it low.
		_delay_ms(1000); // waits 1 second

	}
}
