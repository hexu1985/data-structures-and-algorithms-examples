
libraries := 
programs := ch1 ch2 ch3 ch4 ch5 ch6

.PHONY: all $(programs) $(libraries)
all: $(programs)

$(programs) $(libraries):
	$(MAKE) --directory=$@ $(TARGET)

# dependency
$(programs): $(libraries)

clean:
	$(MAKE) TARGET=clean
