[
  {
    "id": "e39c9359-f6de-4f42-9106-dc02959b6267",
    "user_id": "84c7662d-29a4-4c8d-a2e7-adb71faff01f",
    "username": "admin",
    "resource_type": "Virtual Machine",
    "violation": "CPU exceeds allowed limit (8 > 4 cores)",
    "request": {
      "resource_type": "Virtual Machine",
      "cpu": 8,
      "ram": 16,
      "storage": 200,
      "region": "US-East"
    },
    "created_at": "2026-03-25T08:50:20.536330"
  },
  {
    "id": "b3c36efe-42b5-4fdb-9977-35232267c533",
    "user_id": "84c7662d-29a4-4c8d-a2e7-adb71faff01f",
    "username": "admin",
    "resource_type": "Virtual Machine",
    "violation": "RAM exceeds allowed limit (16 GB > 8 GB)",
    "request": {
      "resource_type": "Virtual Machine",
      "cpu": 8,
      "ram": 16,
      "storage": 200,
      "region": "US-East"
    },
    "created_at": "2026-03-25T08:50:20.536599"
  },
  {
    "id": "0bee54df-6322-42f5-97c4-a60065fbd13f",
    "user_id": "84c7662d-29a4-4c8d-a2e7-adb71faff01f",
    "username": "admin",
    "resource_type": "Virtual Machine",
    "violation": "Storage exceeds allowed limit (200 GB > 100 GB)",
    "request": {
      "resource_type": "Virtual Machine",
      "cpu": 8,
      "ram": 16,
      "storage": 200,
      "region": "US-East"
    },
    "created_at": "2026-03-25T08:50:20.536887"
  },
  {
    "id": "c2cc8a1e-7b09-4be8-8db8-74486e6b4011",
    "user_id": "84c7662d-29a4-4c8d-a2e7-adb71faff01f",
    "username": "admin",
    "resource_type": "Virtual Machine",
    "violation": "Region 'US-East' is not allowed. Allowed regions: Asia, India",
    "request": {
      "resource_type": "Virtual Machine",
      "cpu": 8,
      "ram": 16,
      "storage": 200,
      "region": "US-East"
    },
    "created_at": "2026-03-25T08:50:20.537502"
  },
  {
    "id": "5f0149dd-4c37-41fa-bfe3-a6f128827d27",
    "user_id": "dbad2876-b507-4f94-8dac-58cc99fccc2a",
    "username": "aadarsh",
    "resource_type": "Storage",
    "violation": "CPU exceeds allowed limit (12 > 4 cores)",
    "request": {
      "resource_type": "Storage",
      "cpu": 12,
      "ram": 8,
      "storage": 50,
      "region": "Asia"
    },
    "created_at": "2026-03-25T09:05:28.153190"
  },
  {
    "id": "7420ba9a-a2ec-4b47-9ae6-28389c43d703",
    "user_id": "dbad2876-b507-4f94-8dac-58cc99fccc2a",
    "username": "aadarsh",
    "resource_type": "Storage",
    "violation": "Region 'US-East' is not allowed. Allowed regions: Asia, India",
    "request": {
      "resource_type": "Storage",
      "cpu": 2,
      "ram": 4,
      "storage": 10,
      "region": "US-East"
    },
    "created_at": "2026-03-25T09:06:15.294828"
  }
]