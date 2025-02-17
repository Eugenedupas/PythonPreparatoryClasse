class Cplx:
    """Une classe permettant d'effectuer des manipulations
    de base sur les complexes. """
    # ==================================================================== #
    # CONSTRUCTION                                                         #
    # Les noms des attributs sont choisis pour lire aisément les calculs
    # self.re : partie réelle du complexe.
    # self.im : partie imaginaire du complexe.
    # ==================================================================== #
    def __init__(self,x,y):
        self.re = x
        self.im = y
    # ===================================================================== #
    # Représentation du complexe, tenant compte de situations particulières #
    # La méthode spéciale __repr__ doit renvoyer une chaîne de caractères ! #
    # ===================================================================== #
    def __repr__(self):
        s = str(self.re)
        if self.im == 0:
            return s
        elif self.re == 0:
            s = str(self.im) + 'i'
        elif self.im < 0 :
            s += ' - ' + str(-self.im) + 'i'
        else :
            s += ' + ' + str(self.im) + 'i'
        return s

    # ================================================================= #
    # Surcharge de l'opérateur d'addition + avec __add__ et __radd__    #
    # ================================================================= #
    # Méthode spéciale __add__ : surcharge de l'opérateur + afin de pouvoir
    # sommer un complexe et un autre nombre grâce au symbole +.
    # On traite le cas où le PREMIER TERME de l'addition est un complexe.
    def __add__(self,z):
        if type(z) == int or type(z) == float:
            return Cplx(self.re + z,self.im)
        else:
            return Cplx(self.re + z.re,self.im + z.im)

    # Méthode spéciale __radd__ : surcharge de l'opérateur + afin de
    # pouvoir sommer un autre nombre et un complexe grâce au symbole +.
    # On traite le cas où le DEUXIEME TERME de l'addition est un complexe,
    # MAIS PAS LE PREMIER.
    def __radd__(self,z):
        # si on utilise __radd__, c'est que z n'est pas un complexe
        # z est forcément un entier ou un flottant
        return Cplx(self.re + z,self.im)
    def __neg__(self):
        return Cplx(-self.re,-self.im)
    def __sub__(self,z):
        if type(z)==int or type(z)==float:
            return Cplx(self.re-z,self.im)
        else:
            return Cplx(self.re-z.re,self.im-z.im)
    def __rsub__(self,z):
        return Cplx(self.re-z,self.im)

    def __mul__(self,z):
        if type(z)==int or type(z)==float:
            return Cplx(self.re*z,self.im*z)
        else:
            return Cplx(self.re*z.re-self.im*z.im,self.re*z.im+self.im*z.re)
    def __rmul__(self,z):
        return Cplx(self.re*z,self.im*z)
    def __truediv__(self,z):
        if z==0:
            raise ValueError('divise par 0')
        if type(z)==int or type(z)==float:
            return Cplx(self.re/z,self.im/z)
        else:
            return Cplx((self.re*z.re+self.im*z.im)/z.module()**2,(self.im*z.re-self.re*z.im)/z.module()**2)
    def __rtruediv__(self,z):
        return Cplx(z*self.re/self.module()**2,-z*self.im/self.module()**2)

    def module(self):
        """Renvoie le module du complexe
        """
        return (self.re**2 + self.im**2)**0.5

    def argument(self):
        """Renvoie, s'il est défini, l'argument du complexe,
        compris entre -pi et pi,
        """
        from math import atan2
        if self.re != 0 or self.im != 0:
            return atan2(self.im,self.re)
        else:
            raise ValueError('Argument de zéro non défini')

    def conj(self):
        return Cplx(self.re, -self.im)

    def inv(self):
        mcarre=self.re**2 + self.im**2
        if mcarre==0:
            raise ValueError('complexe nul')
        return Cplx(self.re/mcarre,-self.im/mcarre)

def u(x):
    return x