# Protocol

## Connection
- Transport: TCP
- Port: `8080`
- Format: JSON UTF-8
- Delimiter: newline (`\n`)

## Services
- `char_count`
- `word_count`
- `reverse`
- `remove_vowels`
- `matrix_3x3`

## Request
```json
{
  "type": "request",
  "request_id": "1",
  "service": "char_count",
  "params": {
    "text": "hello"
  }
}
```

## Response
```json
{
  "type": "response",
  "request_id": "1",
  "service": "char_count",
  "status": "success",
  "result": 5
}
```

## ACK
Client memeriksa hasil server lalu mengirim acknowledgement.

```json
{
  "type": "ack",
  "request_id": "1",
  "correct": true
}
```

Jika `correct` bernilai `false`, server menonaktifkan service tersebut.

## Disabled Service
```json
{
  "status": "error",
  "message": "service_disabled"
}
```

## Fault Injection
Server memiliki peluang `30%` untuk mengirim hasil yang salah.

## Shutdown
Jika semua service nonaktif, server menghentikan proses.
