#include <avr/io.h>
#include <util/delay.h>

int main(void) {
    // Set up the Data Direction Register for Port B
    // For Arduino Mega 2560, the onboard LED is connected to PB7
    DDRB |= (1 << DDB7); // Set the DDRB7 bit to 1 to set PB7 as an output

    // Main loop
    while(1) {
        // Turn on the LED
        PORTB |= (1 << PORTB7); // Set the PORTB7 bit to 1 to turn on the LED
        _delay_ms(1000); // Wait for 1000 milliseconds (1 second)

        // Turn off the LED
        PORTB &= ~(1 << PORTB7); // Clear the PORTB7 bit to turn off the LED
        _delay_ms(1000); // Wait for 1000 milliseconds (1 second)
    }
}

