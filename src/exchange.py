# ------------------------------------------------------
# Validate GeoJSON FeatureCollection
# ------------------------------------------------------

def validate_feature_collection(data):

    if data.get("type") != "FeatureCollection":
        raise ValueError("Expected FeatureCollection")

    features = data.get("features")

    if not isinstance(features, list):
        raise ValueError("Features must be a list")

    for feature in features:

        if feature.get("type") != "Feature":
            raise ValueError("Invalid feature type")

        if not feature.get("id"):
            raise ValueError("Feature is missing an ID")

        if feature.get("geometry") is None:
            raise ValueError("Feature is missing geometry")

        if not isinstance(feature.get("properties"), dict):
            raise ValueError("Properties must be an object")

    return True

# ------------------------------------------------------
# Build GeoJSON FeatureCollection from parcels
# ------------------------------------------------------

def build_feature_collection(parcels):
    return {
        "type": "FeatureCollection",
        "features": [
            parcel.to_feature()
            for parcel in parcels
        ],
    }
