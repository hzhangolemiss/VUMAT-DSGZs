JOB_ID = Job-1

# Nothing to touch here after

all: clean pre cae-runscript keep-odb-cae-jnl extract plot

pre:
	mkdir -p $(shell pwd)/abq_run

cae-runscript:
	cd $(shell pwd)/abq_run && \
	abaqus cae noGUI=../CompShock.py

keep-odb-cae-jnl:
	# Clean files while keeping .odb
	find $(shell pwd)/abq_run -type f -not -name '*.odb' -not -name '*.cae' -not -name '*.jnl' -delete

extract:
	@cd $(shell pwd)/abq_run && \
	abaqus python ../../../Python/AbaqusExtract.py

plot:
	@cd $(shell pwd)/abq_run && \
	python3 ../../../Python/replaceString.py $(JOB_ID) $(JOB_ID)_ $(JOB_ID)- && \
	python3 ../../../Python/PlotCurves.py

clean:
	@if [ -d "$(shell pwd)/abq_run/" ]; then \
	    echo "Cleaning: $(PWD)/abq_run/" && \
	    find $(shell pwd)/abq_run -type f -not -name '*.png' -delete; \
	fi

subclean: clean
