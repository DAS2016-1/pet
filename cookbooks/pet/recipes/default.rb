execute 'apt-get update'
package 'vim'
package 'postgresql-9.4'
package 'postgresql-9.4-debversion'
package 'python-argparse' 
package 'python-debian' 
package 'python-debianbts' 
package 'python-inotifyx' 
package 'python-paste' 
package 'python-psycopg2' 
package 'python-pyramid' 
package 'python-sqlalchemy'
package 'python-subversion'
package 'python-pip' 
package 'wget'

execute 'pip install pyramid_chameleon'

user 'pet' do
  action :create
end

cookbook_file '/etc/postgresql/9.4/main/postgresql.conf' do
  owner 'postgres'
  group 'postgres'
  mode '644'
  action :create
end

cookbook_file '/etc/postgresql/9.4/main/pg_hba.conf' do
  owner 'postgres'
  group 'postgres'
  mode '640'
  action :create
end

service 'postgresql' do
  action [:start, :enable]
end

execute "createuser --createdb pet" do
  user "postgres"
  action :run
  ignore_failure true
end

execute "createdb pet" do
  user "pet"
  action :run
  ignore_failure true
end

execute "psql pet < /usr/share/postgresql/9.4/contrib/debversion.sql" do
  user "postgres"
  action :run
  ignore_failure true
end

cookbook_file '/etc/hosts' do
  owner 'root'
  group 'root'
  mode '644'
  action :create
end

service 'postgresql' do
  action :restart
end

execute "/vagrant/pet-update -c" do
  user "pet"
  action :run
end

execute "database tables" do
  command "psql pet --command \"INSERT INTO team (name, maintainer, url) VALUES ('pkg-perl', 'Debian Perl Group <pkg-perl-maintaine    rs@lists.alioth.debian.org>', 'http://pkg-perl.alioth.debian.org/'); INSERT INTO repository (name, type, root, web_root, team_id) VALUES     ('git','git','https://pet.alioth.debian.org/pet2-data/pkg-perl/git-pkg-perl-packages.json','http://anonscm.debian.org/gitweb/?p=pkg-per    l/packages', 1); INSERT INTO package (name, repository_id) VALUES ('clive', 1); INSERT INTO archive (name, url, web_root) VALUES ('debia    n', 'http://cdn.debian.net/debian', 'http://packages.qa.debian.org/'); INSERT INTO suite (archive_id, name) VALUES (1, 'unstable');\""
  user "pet"
  action :run
end

execute "/srv/pet/pet-serve" do
  user "pet"
  action :run
end

