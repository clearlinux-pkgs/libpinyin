#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpinyin
Version  : 2.7.92
Release  : 15
URL      : https://sourceforge.net/projects/libpinyin/files/libpinyin/libpinyin-2.7.92.tar.gz
Source0  : https://sourceforge.net/projects/libpinyin/files/libpinyin/libpinyin-2.7.92.tar.gz
Summary  : Library to deal with pinyin
Group    : Development/Tools
License  : GPL-3.0
Requires: libpinyin-bin = %{version}-%{release}
Requires: libpinyin-lib = %{version}-%{release}
Requires: libpinyin-license = %{version}-%{release}
Requires: libpinyin-man = %{version}-%{release}
BuildRequires : kyotocabinet-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(kyotocabinet)

%description
libpinyin
Library to deal with pinyin.
The libpinyin project aims to provide the algorithms core for intelligent sentence-based Chinese pinyin input methods.

%package bin
Summary: bin components for the libpinyin package.
Group: Binaries
Requires: libpinyin-license = %{version}-%{release}

%description bin
bin components for the libpinyin package.


%package dev
Summary: dev components for the libpinyin package.
Group: Development
Requires: libpinyin-lib = %{version}-%{release}
Requires: libpinyin-bin = %{version}-%{release}
Provides: libpinyin-devel = %{version}-%{release}
Requires: libpinyin = %{version}-%{release}

%description dev
dev components for the libpinyin package.


%package lib
Summary: lib components for the libpinyin package.
Group: Libraries
Requires: libpinyin-license = %{version}-%{release}

%description lib
lib components for the libpinyin package.


%package license
Summary: license components for the libpinyin package.
Group: Default

%description license
license components for the libpinyin package.


%package man
Summary: man components for the libpinyin package.
Group: Default

%description man
man components for the libpinyin package.


%prep
%setup -q -n libpinyin-2.7.92
cd %{_builddir}/libpinyin-2.7.92

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666190419
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-dbm=KyotoCabinet
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1666190419
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libpinyin
cp %{_builddir}/libpinyin-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libpinyin/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/libpinyin/data/addon_phrase_index.bin
/usr/lib64/libpinyin/data/addon_pinyin_index.bin
/usr/lib64/libpinyin/data/art.bin
/usr/lib64/libpinyin/data/bigram.db
/usr/lib64/libpinyin/data/culture.bin
/usr/lib64/libpinyin/data/economy.bin
/usr/lib64/libpinyin/data/gb_char.bin
/usr/lib64/libpinyin/data/gbk_char.bin
/usr/lib64/libpinyin/data/geology.bin
/usr/lib64/libpinyin/data/history.bin
/usr/lib64/libpinyin/data/life.bin
/usr/lib64/libpinyin/data/merged.bin
/usr/lib64/libpinyin/data/nature.bin
/usr/lib64/libpinyin/data/opengram.bin
/usr/lib64/libpinyin/data/people.bin
/usr/lib64/libpinyin/data/phrase_index.bin
/usr/lib64/libpinyin/data/pinyin_index.bin
/usr/lib64/libpinyin/data/science.bin
/usr/lib64/libpinyin/data/society.bin
/usr/lib64/libpinyin/data/sport.bin
/usr/lib64/libpinyin/data/table.conf
/usr/lib64/libpinyin/data/technology.bin

%files bin
%defattr(-,root,root,-)
/usr/bin/gen_binary_files
/usr/bin/gen_unigram
/usr/bin/import_interpolation

%files dev
%defattr(-,root,root,-)
/usr/include/libpinyin-2.7.92/novel_types.h
/usr/include/libpinyin-2.7.92/pinyin.h
/usr/include/libpinyin-2.7.92/pinyin_custom2.h
/usr/lib64/libpinyin.so
/usr/lib64/pkgconfig/libpinyin.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpinyin.so.15
/usr/lib64/libpinyin.so.15.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libpinyin/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/libpinyin.1
