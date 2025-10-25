.PHONY: fmt lint test ci
fmt:; black migrator; ruff migrator --fix || true; cargo fmt --manifest-path rust/Cargo.toml
lint:; ruff migrator || true; cargo clippy --manifest-path rust/Cargo.toml -- -D warnings
test:; cargo test --manifest-path rust/Cargo.toml
ci: fmt lint test
