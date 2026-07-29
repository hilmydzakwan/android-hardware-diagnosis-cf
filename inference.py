# ==============================
#  inference.py
#  Mesin Certainty Factor
# ==============================

# --------------------------------------
# Rumus kombinasi CF (standar literatur)
# --------------------------------------
def combine_cf(cf1, cf2):
    """Menggabungkan dua nilai CF."""
    if cf1 >= 0 and cf2 >= 0:
        return cf1 + cf2 * (1 - cf1)
    elif cf1 < 0 and cf2 < 0:
        return cf1 + cf2 * (1 + cf1)
    else:
        return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))


# ----------------------------------------------------
# Hitung CF dari satu gejala: CF_user × CF_rule_pakar
# ----------------------------------------------------
def hitung_cf_gejala(cf_user, cf_rule):
    return cf_user * cf_rule


# -------------------------------------------------------------------------
# Hitung CF total untuk tiap kerusakan (gabungan beberapa gejala sekaligus)
# -------------------------------------------------------------------------
def hitung_cf_total(user_input, rulesCF):
    """
    user_input = { "g1": 0.8, "g2": 1.0, ... }
    rulesCF     = dataset dari knowledge.py
    """

    hasil_per_kerusakan = {}

    # Loop semua gejala yang diinput user
    for gejala, nilai_user in user_input.items():
        if gejala not in rulesCF:
            continue

        # Ambil semua kemungkinan kerusakan pada gejala tsb
        kerusakan_map = rulesCF[gejala]

        for kerusakan, cf_rule in kerusakan_map.items():

            # Hitung CF gejala = CF_user × CF_rule_pakar
            cf_gejala = hitung_cf_gejala(nilai_user, cf_rule)

            # Jika kerusakan belum pernah dihitung → masukkan langsung
            if kerusakan not in hasil_per_kerusakan:
                hasil_per_kerusakan[kerusakan] = cf_gejala
            else:
                # Sudah ada nilai sebelumnya → kombinasikan
                hasil_per_kerusakan[kerusakan] = combine_cf(
                    hasil_per_kerusakan[kerusakan],
                    cf_gejala
                )

    return hasil_per_kerusakan


# --------------------------------
# Interpretasi level hasil CF
# --------------------------------
def interpretasi_cf(cf_value):
    if cf_value >= 0.80:
        return "Tingkat Tinggi"
    elif cf_value >= 0.60:
        return "Tingkat Sedang"
    elif cf_value >= 0.40:
        return "Tingkat Rendah"
    else:
        return "Tidak Signifikan"
