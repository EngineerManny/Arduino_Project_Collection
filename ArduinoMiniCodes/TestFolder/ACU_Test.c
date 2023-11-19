#include <avr/io.h>
#include <util/delay.h>

int main(void) {
    DDRB |= (1 << DDB7); // Set PB7 as an output
    while(1) {
        PORTB |= (1 << PORTB7);  // Turn LED on
        _delay_ms(1000);         // Wait
        PORTB &= ~(1 << PORTB7); // Turn LED off
        _delay_ms(1000);         // Wait
    }
}

