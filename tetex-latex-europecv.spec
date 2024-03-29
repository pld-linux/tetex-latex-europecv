
%define	short_name	europecv
%define	texhash		[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Unofficial class for European curricula vitae
Summary(pl.UTF-8):	Nieoficjalna klasa dla europejskiego CV
Name:		tetex-latex-%{short_name}
Version:	1.0.0
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://www.ctan.org/tex-archive/macros/latex/contrib/%{short_name}.zip
# Source0-md5:	6c9f7fb958cbf0e3d5bbc4a9c9a77deb
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
Requires:	tetex-latex-unicode
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The europecv class is an unofficial LaTeX implementation of the
standard model for curricula vitae (the Europass CV) as recommended by
the European Commission. Although primarily intended for users in the
European Union, the class is flexible enough to be used for any kind
of curriculum vitae.

The class has localisations for all the official languages of the EU
(plus Catalan); the class has options permitting input in UTF-8 and
KOI8-R.

%description -l pl.UTF-8
Klasa europecv jest nieoficjalną LaTeXową implementacją standardowego
modelu curricula vitae (Europass CV) według zaleceń Komisji
Europejskiej. Pomimo, iż przeznaczona jest dla użytkowników z krajów
Unii Europejskiej, klasa ta jest na tyle elastyczna, że może być użyta
w dowolnym rodzaju curriculum vitae.

Klasa posiada tłumaczenia dla wszystkich oficjalnych języków Unii
Europejskiej (oraz katalońskiego); klasa posiada możliwość zezwalania
na dane wejściowe w formatach UTF-8 oraz KOI8-R.

%prep
%setup -q -n %{short_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install *.def *.pdf *.eps *.cls *.tex $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc examples/ templates/
%{_datadir}/texmf/tex/latex/%{short_name}
