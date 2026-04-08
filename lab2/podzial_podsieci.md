# Podział podsieci – 10.10.200.0/23

## Dane wejściowe

Sieć bazowa: **10.10.200.0/23**

### Zapotrzebowanie działów

| Dział        | Liczba urządzeń |
| ------------ | --------------- |
| Sieć gościnna | 100             |
| IT           | 50              |
| HR           | 12              |
| Księgowość   | 10              |

---

## Zapas adresów (over-provisioning)

(+50% + 1 adres dla routera)

| Dział        | Wymagana liczba hostów |
| ------------ | ---------------------- |
| Sieć gościnna | 151                   |
| IT           | 76                    |
| HR           | 19                    |
| Księgowość   | 16                    |

---

## Dobór masek

| Dział         | Prefiks | Maks. hostów |
| ------------- | ------- | ------------ |
| Sieć gościnna | /24     | 254          |
| IT            | /25     | 126          |
| HR            | /27     | 30           |
| Księgowość    | /27     | 30           |

---

# Struktura podziału

## Wersja A (z pozostawioną rezerwą)

```
10.10.200.0/23:
	- 10.10.200.0/24:
		- 10.10.200.0/25:
			- 10.10.200.0/26:
				- 10.10.200.0/27 (HR, 30)
				- 10.10.200.32/27 (KSIĘGOWOŚĆ, 30)
			- 10.10.200.64/26 (rezerwa, 62)
		- 10.10.200.128/25 (IT, 126)
	- 10.10.201.0/24 (GOŚCIE, 254)
```

---

## Wersja B (pełne wykorzystanie przestrzeni)

```
10.10.200.0/23:
	- 10.10.200.0/24:
		- 10.10.200.0/25:
			- 10.10.200.0/26 (HR, 62)
			- 10.10.200.64/26 (KSIĘGOWOŚĆ, 62)
		- 10.10.200.128/25 (IT, 126)
	- 10.10.201.0/24 (GOŚCIE, 254)
```

---

# Szczegóły podsieci

## GOŚCIE (10.10.201.0/24)

* adres sieci: 10.10.201.0  
* pierwszy host: 10.10.201.1  
* ostatni host: 10.10.201.254  
* broadcast: 10.10.201.255  
* liczba hostów: 254  

**Zapas:**

* względem minimum (100): +154  
* względem wymaganego (151): +103  

---

## IT (10.10.200.128/25)

* adres sieci: 10.10.200.128  
* pierwszy host: 10.10.200.129  
* ostatni host: 10.10.200.254  
* broadcast: 10.10.200.255  
* liczba hostów: 126  

**Zapas:**

* względem minimum (50): +76  
* względem wymaganego (76): +50  

---

## HR (10.10.200.0/27)

* adres sieci: 10.10.200.0  
* pierwszy host: 10.10.200.1  
* ostatni host: 10.10.200.30  
* broadcast: 10.10.200.31  
* liczba hostów: 30  

**Zapas:**

* względem minimum (12): +18  
* względem wymaganego (19): +11  

---

## KSIĘGOWOŚĆ (10.10.200.32/27)

* adres sieci: 10.10.200.32  
* pierwszy host: 10.10.200.33  
* ostatni host: 10.10.200.62  
* broadcast: 10.10.200.63  
* liczba hostów: 30  

**Zapas:**

* względem minimum (10): +20  
* względem wymaganego (16): +14  

---

# Niewykorzystane zakresy (wersja A)

* 10.10.200.64/26 → 64 adresy  

**Łącznie wolnych: 64 adresy IP**
