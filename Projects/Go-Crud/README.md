## Build CRUD app with Go & Gin

- Initialize project

```sh
go mod init primetimetran/crud-service-gin
```

- Install dep

```sh
go get .
```

- Start program

```sh
go run .
```

- Read items

```sh
curl http://localhost:8080/albums
```

- Create album item

```sh
curl http://localhost:8080/albums \
	--include \
	--header "Content-Type: application/json" \
	--request "POST" \
	--data '{"id": "4","title": "The Modern Sound of Betty Carter","artist": "Betty Carter","price": 49.99}'
```

- Read specific item

```sh
curl http://localhost:8080/albums/2
```

## Resources

- https://go.dev/doc/tutorial/web-service-gin
