from oracle import *
from helper import *

# get x^-1 (inverse)
def getInverse(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = getInverse(b % a, a)
        return (g, x - (b // a) * y, y)


def main():

    n = 119077393994976313358209514872004186781083638474007212865571534799455802984783764695504518716476645854434703350542987348935664430222174597252144205891641172082602942313168180100366024600206994820541840725743590501646516068078269875871068596540116450747659687492528762004294694507524718065820838211568885027869

    e = 65537

    Oracle_Connect()

    msg = "Crypto is hard --- even schemes that look complex can be broken"

    m = ascii_to_int(msg)

    # Since we know M = k*m -> {0x00m0x00m = (m * x + m = (x+1)*m -> x+1=k)}
    # we can do the following M = m/2 * 2 * k, so we get (m/2)d^ * (2)^d * (k)^d (mod N)
    # also we know that sign(2) -> (2)^d * (k)^d (mod N) and sign(m/2) -> (m/2)^d * (k)^d (mod N)
    # so therefor we get: (m/2)d^ * (2)^d * (k)^d (mod N) -> (m/2)^d * sign(2) (mod N)
    # now we need to find out ((k)^d)^-1 (mod N) to get (m/2)^d (mod N)|  (m/2)^d = sign(m/2) * ((k)^d)^-1 (mod N) 
    # first we need to find out (k)^d (mod N) and that is sign(1), because sign(1) -> (1)^d * (k)^d (mod N)

    signOfOne = Sign(1) 
    g, signOfOneInverse, y = getInverse(signOfOne, n)
    signOfOneInverse = signOfOneInverse % n

    signOfHalfm = Sign(m/2) % n

    fPart = (signOfHalfm * signOfOneInverse) % n
    sPart = Sign(2) % n

    signOfMessage = (fPart * sPart) % n

    # if Verify(m, signOfMessage):
    #     print "Oracle is working properly!"

    Oracle_Disconnect()
    
    print(signOfMessage)


if __name__ == '__main__':
    main()