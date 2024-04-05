import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException
import os

# Define your Spotify client credentials
client_id = "9d02d2a468c242b4b211a166cb98fac5"
client_secret = "4d3c3289d93a4128a895e6bd931ede1e"
redirect_uri = 'http://localhost:8000/callback'


# Create a Spotify client instance with authorization and custom cache
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read playlist-read-private playlist-modify-public'))

def rdcmd(playlist_id):
    import os
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth

    # Define your Spotify client credentials
    client_id = "799ad76dc8b84d36aafe716062c193f3"
    client_secret = "551d48ca50a046d880c56f0cb9ac4b8e"
    redirect_uri = 'http://localhost:8000/callback'

    # Create a Spotify client instance with authorization and custom cache
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='playlist-modify-public'))

    def remove_duplicates(playlist_id):
        # Get the playlist tracks
        playlist_tracks = []
        results = sp.playlist_tracks(playlist_id)
        playlist_tracks.extend(results['items'])

        # Iterate through additional pages if available
        while results['next']:
            results = sp.next(results)
            playlist_tracks.extend(results['items'])

        # Create a set to store unique track pairs
        unique_track_pairs = set()

        # Create a set to store unique track ids
        unique_ids = set()

        # Create a list to store duplicate track positions
        duplicate_positions = []

        # Create a list to store duplicate track ids
        duplicate_ids = []
        # Iterate over the tracks in the playlist
        for i, track in enumerate(playlist_tracks):
            track_artist = track['track']['artists'][0]['name']
            track_name = track['track']['name']
            track_pair = (track_artist, track_name)
            track_id = track['track']['id']
            id_tuple = (track_pair, track_id)
            if track_pair in unique_track_pairs:
                # Add the duplicate track position to the list
                duplicate_positions.append(i)
                duplicate_ids.append(id_tuple)
            else:
                # Add the track pair to the set
                unique_track_pairs.add(track_pair)
                unique_ids.add(id_tuple)

        # Remove the duplicate tracks from the playlist in batches
        if duplicate_positions:
            batch_size = 100  # Number of tracks to remove per request
            total_duplicates = len(duplicate_positions)
            num_batches = (total_duplicates + batch_size - 1) // batch_size  # Round up to the nearest integer

            for i in range(num_batches):
                start_idx = i * batch_size
                end_idx = (i + 1) * batch_size
                batch_positions = duplicate_positions[start_idx:end_idx]
                

                # Remove the duplicate tracks in the current batch
                batch_track_ids = [playlist_tracks[position]['track']['id'] for position in batch_positions]
                sp.playlist_remove_all_occurrences_of_items(playlist_id, batch_track_ids)

            print("Duplicates removed successfully.")
        else:
            print("No duplicates found in the playlist.")


        return playlist_tracks, unique_ids, duplicate_ids



    def check_dupes(duplicate_ids, unique_ids):
    # Create a new list to store non-duplicate items
        filtered_list = []

        # Iterate over the duplicate_ids list with index using enumerate
        for t, d in enumerate(duplicate_ids):
            if d in unique_ids:
                # Add non-duplicate items to the filtered list
                if d not in filtered_list:
                    filtered_list.append(d)

        if filtered_list:
            # Separate the list into two lists
            pairs_list, id_list = zip(*filtered_list)

            print(pairs_list)
            print(id_list)

            tracks_to_add = id_list
        else:
            tracks_to_add = []

        return tracks_to_add











    # Say script is starting
    print("Starting ...")

    # Remove duplicates from the playlist

    playlist_tracks, unique_ids, duplicate_ids= remove_duplicates(playlist_id)


    tracks_to_add = check_dupes(duplicate_ids,unique_ids)


    # Add the tracks back to the playlist

    if tracks_to_add:
        batch_size = 100  # Number of tracks to add per request
        num_batches = (len(tracks_to_add) + batch_size - 1) // batch_size  # Round up to the nearest integer

        for i in range(num_batches):
            start_idx = i * batch_size
            end_idx = (i + 1) * batch_size
            batch_tracks = tracks_to_add[start_idx:end_idx]

            sp.playlist_add_items(playlist_id, batch_tracks)

        print("Duplicate tracks added back to the playlist.")
    else:
        print("No duplicate tracks add back to the playlist.")


playlist_mappings = {
    "1": {  # Release Radar
        "source_playlist_id": "spotify:playlist:37i9dQZEVXbh0cIOdUOWZd",
        "destination_playlist_ids": [
            "spotify:playlist:5One87TppPQ9MwiqVdKQxY"
        ]
    },
    "2": {  # Release Radar All
        "source_playlist_id": "spotify:playlist:37i9dQZEVXbh0cIOdUOWZd",
        "destination_playlist_ids": [
            "spotify:playlist:5P7drST9luBzYCMIUDtXsm"
        ]
    },
    "3": {  # Discover Weekly
        "source_playlist_id": "spotify:playlist:37i9dQZEVXcEtf5RqoUIFC",
        "destination_playlist_ids": [
            "spotify:playlist:6tcMhC8Vu5Jxk7BJkcHQk1"
        ]
    },
    "4": {  # Discover Weekly All
        "source_playlist_id": "spotify:playlist:37i9dQZEVXcEtf5RqoUIFC",
        "destination_playlist_ids": [
            "spotify:playlist:5P7drST9luBzYCMIUDtXsm"
        ]
    },
    "5": {  # Daily Mix 1
        "source_playlist_id": "spotify:playlist:37i9dQZF1E35I7u175MhFh",
        "destination_playlist_ids": [
            "spotify:playlist:4t9fGjYh9JDmCq3iHbJpQz"
        ]
    },
    "6": {  # Daily Mix 1 All
        "source_playlist_id": "spotify:playlist:37i9dQZF1E35I7u175MhFh",
        "destination_playlist_ids": [
            "spotify:playlist:5P7drST9luBzYCMIUDtXsm"
        ]
    },
    "7": {  # Daily Mix 2
        "source_playlist_id": "spotify:playlist:37i9dQZF1E39vc8pq80Se4",
        "destination_playlist_ids": [
            "spotify:playlist:3r7qWTW9xPperiuWMEyfP8"
        ]
    },
    "8": {  # Daily Mix 2 All
        "source_playlist_id": "spotify:playlist:37i9dQZF1E39vc8pq80Se4",
        "destination_playlist_ids": [
            "spotify:playlist:5P7drST9luBzYCMIUDtXsm"
        ]
    },
    "9": {  # Daily Mix 3
        "source_playlist_id": "spotify:playlist:37i9dQZF1E37wXGheVUCVG",
        "destination_playlist_ids": [
            "spotify:playlist:1iGgHNrNCoc6OFrn7YigGf"
        ]
    },
    "10": {  # Daily Mix 3 All
        "source_playlist_id": "spotify:playlist:37i9dQZF1E37wXGheVUCVG",
        "destination_playlist_ids": [
            "spotify:playlist:5P7drST9luBzYCMIUDtXsm"
        ]
    },
    "11": {  # Daily Mix 4
        "source_playlist_id": "spotify:playlist:37i9dQZF1E38Z5io3zm3Na",
        "destination_playlist_ids": [
            "spotify:playlist:4IBWxKR5tDbqMuiI2korUJ"
        ]
    },
    "12": {  # Daily Mix 4 All
        "source_playlist_id": "spotify:playlist:37i9dQZF1E38Z5io3zm3Na",
        "destination_playlist_ids": [
            "spotify:playlist:5P7drST9luBzYCMIUDtXsm"
        ]
    },
    "13": {  # Daily Mix 5
        "source_playlist_id": "spotify:playlist:37i9dQZF1E3aaVJr7Nhff0",
        "destination_playlist_ids": [
            "spotify:playlist:5jCqTMsYaiMHbhuEuw5zbM"
        ]
    },
    "14": {  # Daily Mix 5 All
        "source_playlist_id": "spotify:playlist:37i9dQZF1E3aaVJr7Nhff0",
        "destination_playlist_ids": [
            "spotify:playlist:5P7drST9luBzYCMIUDtXsm"
        ]
    },
    "15": {  # Daily Mix 6
        "source_playlist_id": "spotify:playlist:37i9dQZF1E36XD9OfJaW7v",
        "destination_playlist_ids": [
            "spotify:playlist:2wbCQDKnDARLg1gyWc8FE6"
        ]
    },
    "16": {  # Daily Mix 6 All
        "source_playlist_id": "spotify:playlist:37i9dQZF1E36XD9OfJaW7v",
        "destination_playlist_ids": [
            "spotify:playlist:5P7drST9luBzYCMIUDtXsm"
        ]
    }
}





    
def main(sp):
    remove_id = set()
    try:
        sp.current_user()  # Check if the current token is valid
    except SpotifyException as e:
        if e.http_status == 401:  # Token expired
            print("Token expired. Refreshing token...")
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read playlist-read-private playlist-modify-public'))
    for choice, playlists in playlist_mappings.items():
        source_playlist_id = playlists["source_playlist_id"]
        destination_playlist_ids = playlists["destination_playlist_ids"]

        source_playlist = sp.playlist_tracks(source_playlist_id)

        
        for destination_playlist_id in destination_playlist_ids:
            destination_playlist = sp.playlist_tracks(destination_playlist_id)
            destination_track_count = destination_playlist['total']  # Get the total number of tracks in the destination playlist
            
            if destination_track_count >= 10000: #If playlist at or above track limit make the tracks rollover
                sp.playlist_replace_items(destination_playlist_id, [])  # Delete all tracks from the destination playlist
                print(f"Deleted all tracks from {destination_playlist_id} due to reaching the limit.")
                
                # No need to check for duplicates, add all tracks from the source playlist
                source_track_uris = [track['track']['uri'] for track in source_playlist['items']]
                
                if source_track_uris:
                    sp.playlist_add_items(destination_playlist_id, source_track_uris)
                    print(f"Added {len(source_track_uris)} tracks from {source_playlist_id} to {destination_playlist_id}")
                else:
                    print(f"No new tracks to add from {source_playlist_id} to {destination_playlist_id}")
            
            else:
                source_track_uris = [track['track']['uri'] for track in source_playlist['items']]
                
                if source_track_uris:
                    sp.playlist_add_items(destination_playlist_id, source_track_uris)
                    print(f"Added {len(source_track_uris)} tracks from {source_playlist_id} to {destination_playlist_id}")
                else:
                    print(f"No new tracks to add from {source_playlist_id} to {destination_playlist_id}")
            remove_id.add(destination_playlist_id)

    for id in remove_id:
        rdcmd(id)            

if __name__ == "__main__":
    main(sp)