import sys


def wind_chill(t, v):
    return 35.74 + 0.6215 * t - 35.75 * (v**0.16) + 0.4275 * t * (v**0.16)


if len(sys.argv) != 3:
    print("Usage: python WindChill.py <temperature> <wind_speed>")
    sys.exit(1)

t = float(sys.argv[1])
v = float(sys.argv[2])

wc = wind_chill(t, v)
print(f"Wind chill: {wc:.2f}°F")
