package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)
type UserRequest struct {
	UserId string `json:"hey"`
}

func hello(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case "GET":
		io.WriteString(w, "Hello world!")
	case "POST":
		decoder := json.NewDecoder(r.Body)
		var t UserRequest
		err := decoder.Decode(&t)
		if err != nil {
			panic(err)
		}
		fmt.Println(t.UserId)

		println(r.Form.Get("hey"))
		io.WriteString(w, "response world!")

	}
}

func tfidf(w http.ResponseWriter, r *http.Request){
	io.WriteString(w, "search: " + r.FormValue("query"))
}

func main() {
	http.HandleFunc("/login", hello)
	http.HandleFunc("/find", tfidf)
	http.ListenAndServe(":8000", nil)
}
