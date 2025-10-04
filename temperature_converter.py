#!/usr/bin/env python3
"""
Temperature Converter

This module provides functions to convert temperatures between Celsius, Fahrenheit, and Kelvin.
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert temperatures between Celsius, Fahrenheit, and Kelvin.")
    parser.add_argument("value", type=float, help="The temperature value to convert.")
    parser.add_argument("from_unit", choices=["C", "F", "K"], help="The unit of the input temperature (C for Celsius, F for Fahrenheit, K for Kelvin).")
    parser.add_argument("to_unit", choices=["C", "F", "K"], help="The unit to convert to (C for Celsius, F for Fahrenheit, K for Kelvin).")

    args = parser.parse_args()

    if args.from_unit == args.to_unit:
        print(f"{args.value} {args.from_unit}")
        exit(0)

    converters = {
        ("C", "F"): celsius_to_fahrenheit,
        ("F", "C"): fahrenheit_to_celsius,
        ("C", "K"): celsius_to_kelvin,
        ("K", "C"): kelvin_to_celsius,
        ("F", "K"): fahrenheit_to_kelvin,
        ("K", "F"): kelvin_to_fahrenheit,
    }

    converter = converters.get((args.from_unit, args.to_unit))
    if converter:
        result = converter(args.value)
        print(f"{args.value} {args.from_unit} is {result:.2f} {args.to_unit}")
    else:
        print("Invalid conversion.")
        exit(1)