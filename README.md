# Blockchain-Blotto-Game
Simulator to demonstrate Blotto game principles present within smaller-scale 
crypto networks based on total network capacity and the capacity of some 
adversarial collusion network. 

It is well known that Blockchain networks rely on some form of consensus 
algorithm which is determined largely by the computation power of its 
distributed system. However, should some adversarial party be capable of 
taking over majority and perform a "51% attack" on any individual 
cryptocurrency, many transactions could be fraudulently altered in order 
to gain some economic incentive. One particular example of note for a 51% 
attack in blockchain history is that of Bitcoin Gold in May 2018. In this 
attack, one actor managed to control the majority of the currency's 
available hash power. Consequently, over the course of several days as the
attack progressed, the attackers managed to fraudulently aquire roughly $18
million of Bitcoin gold. 

Across all cryptocurrencies, there exists some cumulative hashing power
available from all sources. However, the distribution of this hashing power
is often done in a self-serving manner, based on minimizing difficulty and 
maximizing potential return. This issue leads to an interesting dynamic in
a purely competitive environment. As more miners attempt to mine a specifc
coin, the difficulty of mining that coin goes up, lowering the profitability
of that currency. This feature, in turn, pushes miners to other coins that
may be momentarily more profitable to protect their own interests. However,
if a malicious actor were to arbitrarily drive up the difficulty on a coin
at a temporarily loss, they would displace some computational resources 
within that network. If this attack were completed with sufficient 
computational power, the malicious actor could hypothetically achieve a 
~51% majority, compromising the entire network. 

In order to prevent this from happening, miners must sometimes act
against their own interests to prevent entire currencies from being
compromised. While mining capacity typically lies mostly with the most
valuable coins (i.e. Bitcoin and Ethereum), the smaller coins remain
the most vulnerable. For example, the total hashing power of Bitcoin
is roughly 171.8 EH/s whereas smaller coins such as Bitcoin SV (a hard
fork of Bitcoin Cash which is itself an offshoot of Bitcoin), has a total
network hashing capacity of 745 PH/s. If we consider hardware such as the
WhatsMiner M30S++ at 112 TH/s, we need only 3226 units at around $9.2
million to achieve a majority consensus (assuming we get the full 112 TH/s
on this currency, where in reality it would likely be lower). This number,
while large, is well within the realm of possibility, and for even smaller
currencies, could be much easier. In this hypothetical, how exactly should
mining networks allocate resources to prevent attacks which invariably 
affect everyone on the network in the end? This question is what this
simulator looks to test. 
