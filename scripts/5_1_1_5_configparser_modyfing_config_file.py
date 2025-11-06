import configparser


src_configfile = "data/config.ini"
dst_configfile = "data/config_modify.ini"
with open(src_configfile, "r") as src, open(dst_configfile, "w") as dst:
    content = src.read()
    dst.write(content)

config = configparser.ConfigParser(inline_comment_prefixes="#")
config.read("data/config_modify.ini")

print(config.get("mariadb", "password"))
config.set("mariadb", "password", "Parada20&")
# config['mariadb']['password'] = 'Parada20&'
print(config.get("mariadb", "password"))

print(config.sections())
config.add_section("new_section")
# config.add_section('mariadb')  # DuplicateSectionError
# config.add_section('DEFAULT')  # ValueError
# config.add_section(4)  # TypeError
print(config.sections())

print(config.get("redis", "port"))
config.remove_option("redis", "port")
print(config.get("redis", "port", fallback="No such option."))

print(config.sections())
config.remove_section("redis")
print(config.sections())

with open(dst_configfile, "w") as dst:
    config.write(dst)
