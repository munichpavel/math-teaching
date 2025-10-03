# Vernetnost Vaje, WS 2025-2026

## 2025-10-06

### Uvod

O meni

* Prvic po slovensko
* Zadnjic, ko sem vodil vaje je bilo 2012, ko sem bil postdoc na Humboldt Uni v Berlinu
* Vmes sem delu v bancnistvu, pri Deutsche Bank kot Quantitative Analyst, statistische modellen, potem pa Allianz v Minchenu za 6 let, kjer sem vodil data science ekipe.
* Tudi sem delal za start-ups, sedaj pa vecinoma kot AI / data engineer kot freelancer.
* Ce vas zanima podrocje umetne inteligence, ali res aplikitivno matematiko, se lahko z veseljem govorimo.
* Kabinet je 5.12

Kako bo slo

* Ponavadi jaz eno vajo na tablici
* Potem pa v skupinah, nekdo predstavi resitev
* Najpre lazje vaje, vedno najman ena vaja, ki je tezka kot v kolloqviji


### Vaje

Fokus auf kombinatorik. Na zacetku se bomo zaceli z 'diskretno verjetnost', ki pomeni, da gre za prozece, kjer se lahko samo končno število izidov zdogilo. Koliko jih je za razlicnih izidov je kombinatorik. Tudi v praksi, lahko predstavlja številne probleme s kontinuiranimi številkami kot končnimi izidi, tako da jih razvrsti v skupine ("binning").


#### Definicija

Od https://math.dartmouth.edu/~prob/prob/prob.pdf

**permutacija ene mnozice A**: Naj bo A poljubna končna množica. Permutacija A je ena-na-ena preslikava
A na samo sebe.

**k-permutacija ene mnoznice A**: Naj bo A n-elementna množica in naj bo k celo število med 0 in n. Takrat je k-permutacja množice A urejen seznam podskupine množice A velikosti k.

#### Formule

**Kartezeski produkt mnozic**

Ce ima $|S_i| = n_i$,

$$
| S_1 \times \ldots \times S_k| = n_1 \cdot \ldots \cdot n_k
$$

**stevilo permutacij**

Ce $|S| = n$,

$$
|\{\sigma: S \rightarrow S \ bijective\}| = |S|! = n! = n \cdot (n-1)\cdot \ldots \cdot 1
$$

**stevilo izberov podmnozico velikosti k von n, neurejeno**

$$
{n \choose k} = \frac{n!}{k!(n-k)!}
$$

**permutacije z repeticije tipov**

če imamo $n$ elementov, da so $k_1$ enega tipa (tj. isti ponavljajoči se objekt), $k_2$ drugega tipa, ..., $k_l$ istega tipa (torej različnih tipov objektov),tako da
$n = k_1 + k_2 +···+ k_l$ potem obstaja

$$
\frac{n!}{k_1! k_2! \ldots k_l!}
$$

permutacij, ce dovolimo da se povavlja med vsako skupino.

tudi *multinomial coefficient*.

