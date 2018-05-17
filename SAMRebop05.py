# Attempt to build a program that models and tracks population genetics

# Time Tracker & Websites
## 3/31 - 1 hour
## 4/2 - 3 hours
## https://stackoverflow.com/questions/11487049/python-list-of-lists
## https://stackoverflow.com/questions/18265935/python-create-list-
## with-numbers-between-2-values/36002096

## 4/14 3 hours - Decent breakthrough with long list and skipping. I had tried lists for each trait before.
## https://www.learnpython.org/en/Basic_String_Operations
## 4/15 1 hour - paper
## 4/22 1 hour - paper
## 4/24 2 hours - paper
## 4/26 4 hours - Big breakthrough with breeding. 



### The import random here allows the program to bring in a random choice tool
import random

### Sets the number of alleles for each gene(currently 2) and meiosis range (2 options).
alleles = [0,1]
meiosis = [0,1]

### Asks the user to determine the population size, and records that value.
print("How many Rebops in your population? (Enter value >1)")
pgen_pop = int((input("")))

### Asks the user to determine the number of generations to be run, and records that value.
print("How many breeding cycles would you like to run?")
cycles = int((input("")))

### Creates rebop_geno list, which will be the full library of genomes for the breeding run.
### Also creates pgen_alleles value (total alleles in the pop) Number is 2*number of genes being tracked.
rebop_geno = []
pgen_alleles = 10*pgen_pop

### Fills the library of genomes randomly. This could be tweaked (all heterozygous, for example).
for i in range (pgen_alleles):
    rebop_geno.insert(0,random.choice(alleles))

### Prints out each individual's genome.                
for i in range (pgen_pop):
    print ("P Rebop " + str(i+1)+ " genome:  " + str(rebop_geno [10*i:10*(i+1):1]))

for x in range (cycles):

### Mate selection and gamete formation. mate = selects the start of an individual genome from the
### library, the rebop_geno append commands build the new generation allele by allele from the selected
### parent (i) and the mate by going to each locus and adding either 0 or 1. The mate is then reset.

### The "x*pgen_alleles" is there to adjust based on which generation is breeding.
    for i in range (pgen_pop):
        mate = (10*random.randrange(pgen_pop)+x*pgen_alleles)
        if x <1:
            print ("P Rebop " + str(i+1) + " mates with " "P Rebop " + str(-x*pgen_pop + 1+(int(mate/10))))
        else:
            print ("f" + str(x) + " Rebop " + str(i+1) + " mates with " "f" + str(x) +" Rebop " + str(-x*pgen_pop + 1+(int(mate/10))))
    
        rebop_geno.append (rebop_geno [x*pgen_alleles+((2*5*i)+0+random.choice(meiosis))])
        rebop_geno.append (rebop_geno [((mate)+0+random.choice(meiosis))])
        rebop_geno.append (rebop_geno [x*pgen_alleles+((2*5*i)+2+random.choice(meiosis))])
        rebop_geno.append (rebop_geno [((mate)+2+random.choice(meiosis))])
        rebop_geno.append (rebop_geno [x*pgen_alleles+((2*5*i)+4+random.choice(meiosis))])
        rebop_geno.append (rebop_geno [((mate)+4+random.choice(meiosis))])
        rebop_geno.append (rebop_geno [x*pgen_alleles+((2*5*i)+6+random.choice(meiosis))])
        rebop_geno.append (rebop_geno [((mate)+6+random.choice(meiosis))])
        rebop_geno.append (rebop_geno [x*pgen_alleles+((2*5*i)+8+random.choice(meiosis))])
        rebop_geno.append (rebop_geno [((mate)+8+random.choice(meiosis))])
    
        mate = (10*random.randrange(pgen_pop)+x*pgen_alleles)


    for i in range (pgen_pop):
        print ("f" + str(x+1) + " Rebop " + str(i+1)+ " genome:  " + str(rebop_geno [x*pgen_alleles+10*i:x*pgen_alleles+10*(i+1):1]))

### Attempt to keep program results readable in window by delaying the actual end of the program using an input request.
print("There are the results! Hit enter to end program.")
last_words = (input(""))




                
