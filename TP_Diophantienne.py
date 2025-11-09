Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
...                 print(f"{A} = {B}*{Q} + {R}")
...             print(f"\nPGCD({a},{b}) = {d}")
...             print(f"Pas de solution entière car {d} ne divise pas {c}.\n")
...             print("-" * 60)
...             continue
...
...         d, x0, y0, kx, ky, steps, u, v = result
...         print("\nÉtapes (division euclidienne) :")
...         for A, B, Q, R in steps:
...             print(f"{A} = {B}*{Q} + {R}")
...         print(f"\nPGCD({a},{b}) = {d}")
...         print(f"Coefficients de Bézout : u = {u}, v = {v}")
...         print(f"Vérification : {a}*({u}) + {b}*({v}) = {a*u + b*v}")
...
...         print("\n--- Solution diophantienne ---")
...         print(f"Solution particulière : (x0, y0) = ({x0}, {y0})   (car c/d = {c}//{d} = {c//d})")
...         print("Solution générale :")
...         print(f"x = {x0} + ({kx})*t")
...         print(f"y = {y0} - ({ky})*t")
...         print("pour tout t ∈ Z")
...         print("\nExemples t = -2,-1,0,1,2 :")
...         for t in (-2, -1, 0, 1, 2):
...             xx = x0 + kx * t
...             yy = y0 - ky * t
...             print(f"t={t} -> (x,y)=({xx},{yy})    vérifie {a}*{xx} + {b}*{yy} = {a*xx + b*yy}")
...         print("-" * 60 + "\n")
...
... if __name__ == "__main__":
...     main()
...
=== Résolution ax + by = c (PGCD + Bézout + solution) ===
Tapez 'q' ou 'stop' pour quitter.

a = 9945
b = 3003
c = 39

Étapes (division euclidienne) :
9945 = 3003*3 + 936
3003 = 936*3 + 195
936 = 195*4 + 156
195 = 156*1 + 39
156 = 39*4 + 0

PGCD(9945,3003) = 39
Coefficients de Bézout : u = -16, v = 53
Vérification : 9945*(-16) + 3003*(53) = 39

--- Solution diophantienne ---
Solution particulière : (x0, y0) = (-16, 53)   (car c/d = 39//39 = 1)
Solution générale :
x = -16 + (77)*t
y = 53 - (255)*t
pour tout t ∈ Z

Exemples t = -2,-1,0,1,2 :
t=-2 -> (x,y)=(-170,563)    vérifie 9945*-170 + 3003*563 = 39
t=-1 -> (x,y)=(-93,308)    vérifie 9945*-93 + 3003*308 = 39
t=0 -> (x,y)=(-16,53)    vérifie 9945*-16 + 3003*53 = 39
t=1 -> (x,y)=(61,-202)    vérifie 9945*61 + 3003*-202 = 39
t=2 -> (x,y)=(138,-457)    vérifie 9945*138 + 3003*-457 = 39
------------------------------------------------------------

a =
