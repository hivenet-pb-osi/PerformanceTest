//go:build custom

package env

const HIVE_PLATFORM_ROOT_API = "http://hive-platform:8082"
const HIVE_PLATFORM_API_V1_BASE_URL = HIVE_PLATFORM_ROOT_API + "/v1"
const HIVE_PLATFORM_API_V2_BASE_URL = HIVE_PLATFORM_ROOT_API + "/v2"
const HIVE_HELPER_ROOT_API = "http://agent-helper:8080"
const HIVE_EVENT_ROOT_API = "https://events.dev.hivenet.com"
const BYPASS_SWARM_AND_PLATFORM_ALIGNMENT = false
const BYPASS_BOOTCYCLE = true
const BYPASS_CONTRIBUTION_CHECK = true
const ENABLE_TCP = true

// // Auth0 configuration
// // those values are safe to share (cf auth0 forums - https://community.auth0.com/t/client-id-vs-secret/9558/2)
const AUTH0_DOMAIN = "dev-6te1lp0y.us.auth0.com"
const AUTH0_AUDIENCE = "https://platform.preprod.hivenet.com/"
const AUTH0_CLIENT_ID = "sXCHiI4odN2kv8P45SVcQksKRsybLJaS"

// // MixPanel configurations
const ANALYTICS_TOKEN = "570607cedbc410c9b38c059ce724b094"
const ANALYTICS_API_ENDPOINT = "api-eu.mixpanel.com"
const ANALYTICS_ENABLED = true

// Network swarm isolation
const USE_DATA_PLANE_SWARM_KEY = false
const CONTROL_PLANE_ID = "f346cdde8335178e6a08bf626226198b"
const DATA_PLANE_ID = "23532cd4c06fdff9e3e7072a660c709a"
const CONTROL_PLANE_DHT_PROTOCOL_ID = "/hivenet/" + CONTROL_PLANE_ID + "/1.0.0"
const CONTROL_PLANE_STORAGE_REQUESTS_PUBSUB_TOPIC_ROOM = "/hivenet/" + CONTROL_PLANE_ID + "/pubsub/storage-requests/1.0.0"
const CONTROL_PLANE_RPC_PROTOCOL_ID = "/hivenet/" + CONTROL_PLANE_ID + "/rpc/1.0.0"
const DATA_PLANE_WAN_DHT_PROTOCOL_ID = "/hivenet/" + DATA_PLANE_ID + "/WAN/1.0.0"
const DATA_PLANE_LAN_DHT_PROTOCOL_ID = "/hivenet/" + DATA_PLANE_ID + "/LAN/1.0.0"
