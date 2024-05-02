import wave

def embed_msg(audio, text_message, output_file):
    """
    Embed message into the audio file
    """
    with wave.open(audio, 'rb') as audio: # read
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    binary_msg = ''.join(format(ord(char), '08b') for char in text_message) # binary_conversion
    msg_length = len(binary_msg)

    identifier = '10101010' # assign identifier
    for i in range(8):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(identifier[i])

    length_binary = format(msg_length, '010b') # hide length of message in 10 data samples
    for i in range(10):
        frame_bytes[i+8] = (frame_bytes[i+8] & 254) | int(length_binary[i])

    width_binary = format(10, '010b')  # hide width of message in 10 data samples
    for i in range(10):
        frame_bytes[i+18] = (frame_bytes[i+18] & 254) | int(width_binary[i])

    for i in range(msg_length): # remaining message
        frame_bytes[i+28] = (frame_bytes[i+28] & 254) | int(binary_msg[i])

    with wave.open(output_file, 'wb') as output_audio: # save stego
        output_audio.setparams(audio.getparams())
        output_audio.writeframes(frame_bytes)

def extract_msg(audio):
    """
    Extract message from the stego audio file
    """
    extracted_message = ""

    with wave.open(audio, 'rb') as audio: # read audio
        frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))

    identifier = ''.join([str(frame_bytes[i] & 1) for i in range(8)])
    if identifier != '10101010': # look for hidden message
        print("no hidden message")
        return ""

    msg_length = int(''.join([str(frame_bytes[i] & 1) for i in range(8, 18)]), 2)

    for i in range(28, 28 + msg_length):     # extract using LSB
        extracted_message += str(frame_bytes[i] & 1)
    print(extracted_message)

    secret_message = ''     # change bit to string text
    for i in range(0, len(extracted_message), 8):
        secret_message += chr(int(extracted_message[i:i+8], 2))
    return secret_message

# Example usage with 10,000 words secret message
if __name__ == "__main__":
    embed_msg('assets/cover/bye.wav', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
                               Praesent tincidunt velit nec tortor gravida, quis vestibulum nulla fringilla.\
                                Nam nec ex non enim eleifend ultricies at id mi. Donec feugiat sapien vitae\
                                mauris tristique, nec bibendum nulla laoreet. Sed pretium, magna ut vehicula \
                               sollicitudin, justo sapien ultricies lorem, eget accumsan felis arcu at arcu. \
                               Fusce volutpat fringilla mi, in ultrices quam congue eu. Vestibulum nec odio \
                               eget dui ullamcorper consectetur. Vestibulum ante ipsum primis in faucibus orci\
                                luctus et ultrices posuere cubilia curae; Vestibulum vehicula orci sed libero\
                                finibus, nec faucibus sem luctus. Nullam ultricies velit vel ipsum sodales,\
                                vel tempor purus vulputate. Nulla pharetra vehicula lacus, at lacinia justo \
                               fermentum at. Curabitur malesuada vehicula augue id ultricies. Integer fermentum\
                                ipsum vitae tortor ullamcorper, eget varius sem fermentum. Vivamus auctor, sem\
                                non finibus commodo, orci velit egestas magna, et commodo velit libero eget ante.\
                                Sed auctor, quam ut tempor tincidunt, est metus aliquam mi, nec rhoncus felis orci\
                                id nunc. Phasellus id varius urna.Nulla viverra velit ut neque malesuada, nec \
                               volutpat odio fermentum. Cras viverra vitae nunc sed placerat. Nullam non ipsum \
                               pretium, commodo nisl nec, vestibulum libero. Cras aliquam ultricies elit, nec varius\
                                justo sollicitudin vitae. Aliquam lacinia lorem vel mi dictum luctus. Aenean interdum \
                               hendrerit justo ut gravida. Sed in turpis ac felis iaculis viverra. Curabitur mollis dui\
                                id fringilla rhoncus. Suspendisse vitae malesuada ipsum, nec ultricies nisl. Donec\
                                eleifend eros sit amet tincidunt blandit. In pellentesque, lorem nec vestibulum vehicula,\
                                nulla mauris dignissim sapien, at lobortis neque nisi et risus. Sed vel lectus nec orci\
                                venenatis eleifend id non lorem. Sed fermentum, nunc eget fermentum malesuada, ligula\
                                turpis congue velit, eget egestas turpis arcu non orci. Sed tristique purus sit amet \
                               ipsum auctor, nec tincidunt arcu efficitur. Aliquam erat volutpat. Integer ac massa\
                                quis mauris varius elementum.Mauris vestibulum urna ut sapien fringilla, sed suscipit\
                                lectus dapibus. Vivamus tempor congue urna, id suscipit nisi fermentum ut. Integer nec \
                               metus aliquet, laoreet neque sit amet, commodo sem. Vestibulum ante ipsum primis in faucibus\
                                orci luctus et ultrices posuere cubilia curae; Sed ultricies nunc nec ipsum elementum, eget\
                                ultrices eros posuere. Integer eleifend ipsum vitae velit feugiat, non eleifend turpis\
                                tincidunt. Nam fermentum, tortor in sagittis rutrum, elit neque mattis sapien, eu mollis \
                               mi ipsum et purus. Suspendisse hendrerit magna at elit faucibus, in hendrerit magna eleifend.\
                                Fusce condimentum eros id nulla aliquet posuere. Integer a ex quis ex vehicula finibus.\
                                Suspendisse potenti. Sed interdum est et eros varius suscipit. Suspendisse potenti. \
                               In hac habitasse platea dictumst. Nam vulputate dui non metus rhoncus, ac placerat tortor varius.\
                                Sed ultricies, justo eu consequat rutrum, ipsum eros ultricies nibh, non rutrum quam ante ut nulla.\
                                Proin vehicula ligula nunc, vitae maximus orci luctus nec. Cras sit amet ultricies lectus. Integer et accumsan ex. Aliquam erat volutpat.\
                                Donec ullamcorper, nulla sed pellentesque molestie, mauris velit vehicula justo, vitae vehicula odio magna id mauris. Phasellusvestibulum\
                                massa nec ante fermentum, id vestibulum lorem hendrerit. Vestibulum nec lobortis lorem, eget efficitur nisi. Nulla facilisi. Nam ut ipsum nulla. \
                               Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.\
                                In hac habitasse platea dictumst. Mauris id nisi fermentum, tincidunt purus sed, facilisis enim. \
                               Sed laoreet consequat ligula, at facilisis orci commodo nec. Nam scelerisque dapibus felis eget lacinia.\
                               hasellus gravida fermentum nibh, in tristique nulla. Nullam congue urna nec condimentum sollicitudin. \
                               Integer vitae eros in justo volutpat hendrerit. Pellentesque habitant morbi tristique senectus et \
                               netus et malesuada fames ac turpis egestas. Donec aliquet sollicitudin felis. Morbi et tincidunt nunc,\
                                nec interdum ex. Integer rutrum luctus dolor, at bibendum sapien. Vivamus in purus lacinia, interdum \
                               arcu ut, volutpat metus. Fusce placerat urna sed odio pharetra, in iaculis elit suscipit. Nullam id ex lectus.\
                                Maecenas tempus, tortor eget commodo vestibulum, sapien lorem efficitur libero, a luctus nisl sem ac turpis.\
                                Cras varius mauris nec risus vehicula commodo. In hac habitasse platea dictumst. Vivamus ullamcorper\
                                ligula quis lorem volutpat, at interdum justo consectetur. Ut sed nisi a mi commodo suscipit in ut arcu.\
                               Praesent semper ipsum at libero malesuada tincidunt. Vestibulum quis elit nec leo pellentesque vulputate id at dui\
                               . Vestibulum mollis nec est sed gravida. Vestibulum auctor tempus libero, sit amet aliquam libero vestibulum a.\
                                Aenean id vehicula eros, nec suscipit eros. Curabitur eu sem metus. Sed sit amet libero in nunc congue aliquam. \
                               Morbi placerat, ex nec ullamcorper feugiat, nisi sem condimentum tortor, a interdum turpis ipsum sit amet mauris.\
                                Donec nec lectus lectus. Nam aliquet, quam non maximus ultricies, ligula tortor tempus eros, vel vestibulum \
                               mi justo eu elit. Morbi non efficitur dui. Vivamus quis lectus magna. In ac posuere nulla.\
                                Nullam sit amet leo nec nisl ultrices consequat nec id', 'assets/stego_results/stego_bye.wav')

    extracted_text = extract_msg('assets/stego_results/stego_bye.wav')
    print("Extracted Text:", extracted_text)
