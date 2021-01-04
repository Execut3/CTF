openssl genrsa -out out.key 256
openssl rsa -in out.key -pubout > out.pub
echo "APACTF{T0o0_w3e3e3k}" | openssl rsautl -encrypt -pubin -inkey out.pub > msg.enc