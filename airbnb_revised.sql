-- Added missing created_at and updated_at to the tables

ALTER TABLE users
ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT NOW(),
ADD COLUMN updated_at TIMESTAMP NOT NULL DEFAULT NOW();

ALTER TABLE reservation
ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT NOW(),

ALTER TABLE reservation DROP COLUMN reservation_date;

ALTER TABLE reviews
ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT NOW(),
ADD COLUMN updated_at TIMESTAMP NOT NULL DEFAULT NOW();

ALTER TABLE payment
ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT NOW(),
ADD COLUMN updated_at TIMESTAMP NOT NULL DEFAULT NOW();

-- DECIMAL instead of INTEGER in 'payment'
ALTER TABLE payment
ALTER COLUMN amount TYPE DECIMAL;

-- Changed ON DELETE CASCADE to RESTRICT:
ALTER TABLE reservation
DROP CONSTRAINT IF EXISTS reservation_guest_id_fkey;

ALTER TABLE reservation
ADD FOREIGN KEY (guest_id) REFERENCES users (user_id) ON DELETE RESTRICT;

ALTER TABLE reservation
DROP CONSTRAINT IF EXISTS reservation_room_id_fkey;

ALTER TABLE reservation
ADD FOREIGN KEY (room_id) REFERENCES room (room_id) ON DELETE RESTRICT;

-- Find a user who had the biggest amount of reservations
SELECT u.user_id, u.username, COUNT(r.reservation_id) AS reservation_count
FROM users u
LEFT JOIN reservation r ON u.user_id = r.guest_id
GROUP BY u.user_id, u.username
ORDER BY reservation_count DESC
LIMIT 2;

-- Find a host who earned the biggest amount of money for the last month
WITH HostEarnings AS (
  SELECT r.host_id, SUM(p.amount) AS earnings
  FROM reservation rv
  JOIN payment p ON rv.reservation_id = p.reservation_id
  JOIN room r ON rv.room_id = r.room_id
  WHERE p.payment_date >= DATE_TRUNC('month', NOW()) - INTERVAL '1 month'
  GROUP BY r.host_id
  ORDER BY SUM(p.amount) DESC
  LIMIT 2
)
SELECT u.user_id, u.username, he.earnings
FROM users u
JOIN HostEarnings he ON u.user_id = he.host_id;

-- Find a host with the best average rating
WITH HostAverageRatings AS (
  SELECT r.host_id, AVG(reviews.rating) AS average_rating
  FROM room r
  JOIN reservation rv ON r.room_id = rv.room_id
  JOIN reviews ON rv.reservation_id = reviews.reservation_id
  GROUP BY r.host_id
)
SELECT u.user_id, u.username AS hostname, har.average_rating
FROM "users" u
JOIN HostAverageRatings har ON u.user_id = har.host_id
ORDER BY har.average_rating DESC
LIMIT 2;

