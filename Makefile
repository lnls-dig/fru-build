CC = gcc
CFLAGS = -g -Wall -Wno-packed-bitfield-compat

.PHONY: all clean

all: amc fmc rtm

INCLUDE= -I./src/ -I./user/

COMMON_OBJECTS= src/fru_editor.o

AMC_OBJECTS = src/amc_fru.o $(COMMON_OBJECTS)
FMC_OBJECTS = src/fmc_fru.o $(COMMON_OBJECTS)
RTM_OBJECTS = src/rtm_fru.o $(COMMON_OBJECTS)

HEADERS = fru_editor.h

%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDE) -c $< -o $@

amc: $(AMC_OBJECTS)
	$(CC) $(AMC_OBJECTS) -Wall $(INCLUDE) -o amc_fru

fmc: $(FMC_OBJECTS)
	$(CC) $(FMC_OBJECTS) -Wall $(INCLUDE) -o fmc_fru

rtm: $(RTM_OBJECTS)
	$(CC) $(RTM_OBJECTS) -Wall $(INCLUDE) -o rtm_fru


clean:
	-rm -f src/*.o
	-rm -f amc_fru
	-rm -f fmc_fru
	-rm -f rtm_fru
