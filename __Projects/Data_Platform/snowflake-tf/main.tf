terraform {
  required_providers {
    snowflake = {
      source  = "Snowflake-Labs/snowflake"
      version = "~> 0.61"
    }
  }
}

provider "snowflake" {
  account   = var.snowflake_account
  username  = var.snowflake_username
  password  = var.snowflake_password
  role      = var.snowflake_role
}

resource "snowflake_warehouse" "tf_wh" {
  name            = "NEW_TF_WH"
  warehouse_size  = "XSMALL"
  auto_suspend    = 60
  auto_resume     = true
}
