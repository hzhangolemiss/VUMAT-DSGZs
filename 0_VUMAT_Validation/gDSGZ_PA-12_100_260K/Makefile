ENTITY = CubicElement-Radial

#ABQ_TYPE = D
ABQ_TYPE = DTd

VUMAT_MODEL = $(ENTITY)_VUMAT
VUMAT_JOB_SNRwBiNUM = $(ENTITY)_VUMAT_SNRwBiNUM

NCPUS = 1
NDOMAINS = $(NCPUS)

# Nothing to touch here after

all: clean pre vumat-snrwbinum keep-odb extract plot

pre:
	mkdir -p $(shell pwd)/abq_run_$(ABQ_TYPE)

vumat-snrwbinum:
	# Run VUMAT model using Numerical Newton-Raphson with embedded Bisection
	cd $(shell pwd)/abq_run_$(ABQ_TYPE) && \
	abaqus job=$(VUMAT_JOB_SNRwBiNUM) cpus=$(NCPUS) mp_mode=threads parallel=domain domains=$(NDOMAINS) dynamic_load_balancing=on input=../$(VUMAT_MODEL)_$(ABQ_TYPE).inp user=../../../VUMAT/VUMAT-gDSGZ-SNRwBiNUM.f double=both interactive ask_delete=OFF

keep-odb:
	# Clean files while keeping .odb
	find $(shell pwd)/abq_run_$(ABQ_TYPE) -type f -not -name '*.odb' -not -name '*.png' -delete

extract:
	@cd $(shell pwd)/abq_run_$(ABQ_TYPE) && \
	abaqus python ../../../Python/AbaqusExtract.py

plot:
	@cd $(shell pwd)/abq_run_$(ABQ_TYPE) && \
	python3 ../../../Python/replaceString.py $(VUMAT_JOB_SNRwBiNUM) $(VUMAT_JOB_SNRwBiNUM)_ VUMAT-SNRwBiNUM- && \
	python3 ../../../Python/PlotCurves.py

clean:
	@if [ -d "$(shell pwd)/abq_run_$(ABQ_TYPE)/" ]; then \
	    echo "Cleaning: $(PWD)/abq_run_$(ABQ_TYPE)/" && \
	    find $(shell pwd)/abq_run_$(ABQ_TYPE) -type f -not -name '*.png' -delete; \
	fi

subclean: clean
