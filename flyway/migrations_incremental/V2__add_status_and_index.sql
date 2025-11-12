-- V2__add_status_and_index.sql

ALTER TABLE subscribers
ADD COLUMN status VARCHAR(10) DEFAULT 'active';

CREATE INDEX idx_subscriber_email ON subscribers(email);
