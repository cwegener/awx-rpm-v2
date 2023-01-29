Name:           python-autocommand
Version:        2.2.2
Release:        1%{?dist}
Summary:        A library to create a command-line program from a function

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPLv3
URL:            https://github.com/Lucretiel/autocommand
Source:         %{pypi_source autocommand}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'autocommand' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-autocommand
Summary:        %{summary}

%description -n python3-autocommand %_description


%prep
%autosetup -p1 -n autocommand-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-autocommand -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 2.2.2-1
- Initial package