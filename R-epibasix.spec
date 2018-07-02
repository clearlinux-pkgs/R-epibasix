#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-epibasix
Version  : 1.3
Release  : 2
URL      : https://cran.r-project.org/src/contrib/epibasix_1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/epibasix_1.3.tar.gz
Summary  : Elementary Epidemiological Functions for Epidemiology and
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : clr-R-helpers

%description
common epidemiological problems, ranging from sample size
        estimation, through 2x2 contingency table analysis and basic
        measures of agreement (kappa, sensitivity/specificity).
        Appropriate print and summary statements are also written to
        facilitate interpretation wherever possible.  Source code is
        commented throughout to facilitate modification.  The target
        audience includes advanced undergraduate and graduate students
        in epidemiology or biostatistics courses, and clinical
        researchers.

%prep
%setup -q -c -n epibasix

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530410994

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530410994
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library epibasix
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library epibasix
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library epibasix
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library epibasix|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/epibasix/DESCRIPTION
/usr/lib64/R/library/epibasix/INDEX
/usr/lib64/R/library/epibasix/Meta/Rd.rds
/usr/lib64/R/library/epibasix/Meta/features.rds
/usr/lib64/R/library/epibasix/Meta/hsearch.rds
/usr/lib64/R/library/epibasix/Meta/links.rds
/usr/lib64/R/library/epibasix/Meta/nsInfo.rds
/usr/lib64/R/library/epibasix/Meta/package.rds
/usr/lib64/R/library/epibasix/NAMESPACE
/usr/lib64/R/library/epibasix/R/epibasix
/usr/lib64/R/library/epibasix/R/epibasix.rdb
/usr/lib64/R/library/epibasix/R/epibasix.rdx
/usr/lib64/R/library/epibasix/help/AnIndex
/usr/lib64/R/library/epibasix/help/aliases.rds
/usr/lib64/R/library/epibasix/help/epibasix.rdb
/usr/lib64/R/library/epibasix/help/epibasix.rdx
/usr/lib64/R/library/epibasix/help/paths.rds
/usr/lib64/R/library/epibasix/html/00Index.html
/usr/lib64/R/library/epibasix/html/R.css
