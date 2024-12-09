import subprocess
make_host = ["./out/Default/quic_server", "--quic_response_cache_dir=www.example.org", "--certificate_file=net/tools/quic/certs/out/leaf_cert.pem",
 "--key_file=net/tools/quic/certs/out/leaf_cert.pkcs8"]
subprocess.call(make_host)
