#include "debug.h"
#include "native_wuclasses.h"
#include <avr/io.h>
int counter = 0 ;
void wuclass_seven_segment_setup(wuobject_t *wuobject) {}

void wuclass_seven_segment_update(wuobject_t *wuobject) {
    int val1;
    int val2;
    int val3;
    int val4;
    int tmp;
    counter += 1;
    wkpf_internal_read_property_int16(wuobject, WKPF_PROPERTY_SEVEN_SEGMENT_VALUE1, &val1);
    wkpf_internal_read_property_int16(wuobject, WKPF_PROPERTY_SEVEN_SEGMENT_VALUE2, &val2);
    wkpf_internal_read_property_int16(wuobject, WKPF_PROPERTY_SEVEN_SEGMENT_VALUE3, &val3);
    wkpf_internal_read_property_int16(wuobject, WKPF_PROPERTY_SEVEN_SEGMENT_VALUE4, &val4);
    DDRE |= _BV(5); //digit 1
    DDRG |= _BV(5); //digit 2
    DDRE |= _BV(3); //digit 3
    DDRH |= _BV(3); //digit 4
    DDRH |= _BV(4); // A
    DDRH |= _BV(5); // B
    DDRH |= _BV(6); // C
    DDRB |= _BV(4); // D
    DDRB |= _BV(5); // E
    DDRB |= _BV(6); // f
    DDRB |= _BV(7); // G
    if(counter % 4 == 1){ 
      PORTE |= _BV(5);
      PORTG &= ~_BV(5);
      PORTE &= ~_BV(3);
      PORTH &= ~_BV(3);
      tmp = val1;
      }
    else if(counter % 4 == 2){ 
      PORTE &= ~_BV(5);
      PORTG |= _BV(5);
      PORTE &= ~_BV(3);
      PORTH &= ~_BV(3);
      tmp = val2;
      }
    else if(counter % 4 == 3){ 
      PORTE &= ~_BV(5);
      PORTG &= ~_BV(5);
      PORTE |= _BV(3);
      PORTH &= ~_BV(3);
      tmp = val3;
      }
    else { 
      PORTE &= ~_BV(5);
      PORTG &= ~_BV(5);
      PORTE &= ~_BV(3);
      PORTH |= _BV(3);
      tmp = val4;
      }
    switch (tmp){
        case 0:
            PORTH &= ~_BV(4); //A
            PORTH &= ~_BV(5); //B
            PORTH &= ~_BV(6); //C
            PORTB &= ~_BV(4); //D
            PORTB &= ~_BV(5); //E
            PORTB &= ~_BV(6); //F
            PORTB |= _BV(7); //G
            break;
        case 1:
            PORTH |= _BV(4); //A
            PORTH &= ~_BV(5); //B
            PORTH &= ~_BV(6); //C
            PORTB |= _BV(4); //D
            PORTB |= _BV(5); //E
            PORTB |= _BV(6); //F
            PORTB |= _BV(7); //G
            break;
        case 2:
            PORTH &= ~_BV(4); //A
            PORTH &= ~_BV(5); //B
            PORTH |= _BV(6); //C
            PORTB &= ~_BV(4); //D
            PORTB &= ~_BV(5); //E
            PORTB |= _BV(6); //F
            PORTB &= ~_BV(7); //G
            break;
        case 3:
            PORTH &= ~_BV(4); //A
            PORTH &= ~_BV(5); //B
            PORTH &= ~_BV(6); //C
            PORTB &= ~_BV(4); //D
            PORTB |= _BV(5); //E
            PORTB |= _BV(6); //F
            PORTB &= ~_BV(7); //G
            break;
        case 4:
            PORTH |= _BV(4); //A
            PORTH &= ~_BV(5); //B
            PORTH &= ~_BV(6); //C
            PORTB |= _BV(4); //D
            PORTB |= _BV(5); //E
            PORTB &= ~_BV(6); //F
            PORTB &= ~_BV(7); //G
            break;
        case 5:
            PORTH &= ~_BV(4); //A
            PORTH |= _BV(5); //B
            PORTH &= ~_BV(6); //C
            PORTB &= ~_BV(4); //D
            PORTB |= _BV(5); //E
            PORTB &= ~_BV(6); //F
            PORTB &= ~_BV(7); //G
            break;
        case 6:
            PORTH &= ~_BV(4); //A
            PORTH |= _BV(5); //B
            PORTH &= ~_BV(6); //C
            PORTB &= ~_BV(4); //D
            PORTB &= ~_BV(5); //E
            PORTB &= ~_BV(6); //F
            PORTB &= ~_BV(7); //G
            break;
        case 7:
            PORTH &= ~_BV(4); //A
            PORTH &= ~_BV(5); //B
            PORTH &= ~_BV(6); //C
            PORTB |= _BV(4); //D
            PORTB |= _BV(5); //E
            PORTB |= _BV(6); //F
            PORTB |= _BV(7); //G
            break;
        case 8:
            PORTH &= ~_BV(4); //A
            PORTH &= ~_BV(5); //B
            PORTH &= ~_BV(6); //C
            PORTB &= ~_BV(4); //D
            PORTB &= ~_BV(5); //E
            PORTB &= ~_BV(6); //F
            PORTB &= ~_BV(7); //G
            break;
        case 9:
            PORTH &= ~_BV(4); //A
            PORTH &= ~_BV(5); //B
            PORTH &= ~_BV(6); //C
            PORTB &= ~_BV(4); //D
            PORTB |= _BV(5); //E
            PORTB &= ~_BV(6); //F
            PORTB &= ~_BV(7); //G
            break; 
    
    }
}
