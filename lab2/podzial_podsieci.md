# Podział podsieci – 10.10.200.0/23

## Dane wejściowe

Sieć bazowa: **10.10.200.0/23**

### Zapotrzebowanie działów

| Dział            | Liczba urządzeń |
| ---------------- | --------------- |
| Produkcja        | 80              |
| Administracja    | 40              |
| Dział techniczny | 25              |
| Sprzedaż         | 15              |
| Zarząd           | 8               |

---

## Zapas adresów (over-provisioning)

(+50% + 1 router)

| Dział            | Wymagana liczba hostów |
| ---------------- | ---------------------- |
| Produkcja        | 121                    |
| Administracja    | 61                     |
| Dział techniczny | 38                     |
| Sprzedaż         | 23                     |
| Zarząd           | 13                     |

---

## Dobór masek

| Dział            | Prefiks | Maks. hostów |
| ---------------- | ------- | ------------ |
| Produkcja        | /25     | 126          |
| Administracja    | /26     | 62           |
| Dział techniczny | /26     | 62           |
| Sprzedaż         | /27     | 30           |
| Zarząd           | /28     | 14           |

---

# Struktura podziału

## Wersja A (z rezerwą)

```
10.10.200.0/23:
	- 10.10.200.0/24:
		- 10.10.200.0/25 (PRODUKCJA, 126)
		- 10.10.200.128/25:
			- 10.10.200.128/26 (ADMINISTRACJA, 62)
			- 10.10.200.192/26 (DZIAŁ TECHNICZNY, 62)
	- 10.10.201.0/24:
		- 10.10.201.0/25:
			- 10.10.201.0/26:
				- 10.10.201.0/27 (SPRZEDAŻ, 30)
				- 10.10.201.32/27:
					- 10.10.201.32/28 (ZARZĄD, 14)
					- 10.10.201.48/28 (rezerwa, 14)
			- 10.10.201.64/26 (rezerwa, 62)
		- 10.10.201.128/25 (rezerwa, 126)
```

---

# Szczegóły podsieci

## PRODUKCJA (10.10.200.0/25)

* adres sieci: 10.10.200.0  
* pierwszy host: 10.10.200.1  
* ostatni host: 10.10.200.126  
* broadcast: 10.10.200.127  

---

## ADMINISTRACJA (10.10.200.128/26)

* adres sieci: 10.10.200.128  
* pierwszy host: 10.10.200.129  
* ostatni host: 10.10.200.190  
* broadcast: 10.10.200.191  

---

## DZIAŁ TECHNICZNY (10.10.200.192/26)

* adres sieci: 10.10.200.192  
* pierwszy host: 10.10.200.193  
* ostatni host: 10.10.200.254  
* broadcast: 10.10.200.255  

---

## SPRZEDAŻ (10.10.201.0/27)

* adres sieci: 10.10.201.0  
* pierwszy host: 10.10.201.1  
* ostatni host: 10.10.201.30  
* broadcast: 10.10.201.31  

---

## ZARZĄD (10.10.201.32/28)

* adres sieci: 10.10.201.32  
* pierwszy host: 10.10.201.33  
* ostatni host: 10.10.201.46  
* broadcast: 10.10.201.47  

---

# Wolne zakresy

* 10.10.201.48/28 → 16 adresów  
* 10.10.201.64/26 → 64 adresy  
* 10.10.201.128/25 → 128 adresów  

**Razem wolne: 208 adresów**
