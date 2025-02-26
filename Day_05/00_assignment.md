# HTTP/2 vs HTTP/3 (QUIC)

## Introduction

The Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the web. Over time, HTTP has evolved to improve performance, security, and reliability. This document compares HTTP/2 and HTTP/3 (QUIC), highlighting the problems each solved and providing examples.

## HTTP/2: Overview & Problems Solved

HTTP/2 was introduced to improve the efficiency of web communication by addressing the limitations of HTTP/1.1.

## Key Features of HTTP/2:

1. **Multiplexing**: Allows multiple requests and responses to be sent simultaneously over a single TCP connection, eliminating head-of-line blocking in HTTP/1.1.
2. **Header Compression (HPACK)**: Reduces the size of HTTP headers using compression techniques.
3. **Server Push**: Allows servers to preemptively send resources to the client before they are requested.
4. **Binary Protocol**: Uses binary framing instead of text-based communication, making it more efficient.

## Problems Solved:

- **Reduced Latency**: HTTP/2 eliminates the need for multiple TCP connections, reducing handshake delays.
- **Improved Performance**: By using multiplexing, HTTP/2 prevents requests from blocking each other.
- **Lower Bandwidth Usage**: Header compression reduces unnecessary data transmission.

## Example:

A webpage requiring multiple CSS and JavaScript files in HTTP/1.1 would create separate TCP connections for each request, causing delays. With HTTP/2, all files are fetched simultaneously over a single connection.

## HTTP/3 (QUIC): Overview & Problems Solved

HTTP/3 is the latest version of HTTP and is built on QUIC (Quick UDP Internet Connections) instead of TCP.

## Key Features of HTTP/3:

1. **QUIC Transport Protocol**: Uses UDP instead of TCP for faster and more reliable connections.
2. **Improved Multiplexing**: Prevents head-of-line blocking at the transport layer (TCP in HTTP/2).
3. **Zero Round-Trip Time (0-RTT) Handshakes**: Reduces connection setup time by allowing data transmission in the first request.
4. **Integrated Security (TLS 1.3)**: Provides built-in encryption, reducing security vulnerabilities.

## Problems Solved:

- **TCP Head-of-Line Blocking**: Since HTTP/3 uses QUIC over UDP, packet loss affects only the affected stream instead of blocking all streams.
- **Faster Connections**: QUIC’s 0-RTT handshake enables instant reconnections for returning users.
- **Better Performance on Mobile Networks**: QUIC handles network changes (e.g., switching from Wi-Fi to mobile data) more effectively than TCP.

## Example:

When a user switches from Wi-Fi to mobile data while streaming a video, HTTP/2 would require a new TCP handshake, causing a buffering delay. HTTP/3 (QUIC) resumes the connection without interruption.

## Comparison Table: HTTP/2 vs HTTP/3

| Feature                                | HTTP/2                                | HTTP/3 (QUIC)                  |
| -------------------------------------- | ------------------------------------- | ------------------------------ |
| **Transport Layer**                    | TCP                                   | UDP (QUIC)                     |
| **Multiplexing**                       | Yes, but affected by TCP HOL blocking | Yes, independent streams       |
| **Header Compression**                 | HPACK                                 | QPACK                          |
| **Security**                           | TLS 1.2 / TLS 1.3                     | Always TLS 1.3                 |
| **Connection Setup**                   | Requires TCP handshake                | 0-RTT for faster reconnections |
| **Performance Over Unstable Networks** | Affected by packet loss               | More resilient due to QUIC     |

## Conclusion

HTTP/2 significantly improved web performance over HTTP/1.1 by introducing multiplexing and header compression. However, it still relied on TCP, which caused head-of-line blocking. HTTP/3, built on QUIC, further enhances speed and reliability by eliminating TCP’s limitations, making it ideal for modern web applications.
